import yaml

from numpy import linspace
from orsopy.fileio import model_language as ml
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from PySide6.QtWidgets import QGraphicsScene, QMainWindow

from orso_sample_builder.ui_main_window import Ui_MainWindow

DEFAULT_MODEL = """stack: vacuum | Fe 100 | Si
"""

try:
    import refnx
except ImportError:
    refnx = None


class WorkerSignals(QObject):
    resolved = Signal()
    finished = Signal()


class SimulationWorker(QRunnable):
    """Thread to analyze a sample model in the background, can take a while to find e.g. materials."""

    def __init__(self, sample_model: ml.SampleModel, xray_energy=None):
        super(SimulationWorker, self).__init__()
        self.sample_model = sample_model
        self.x = linspace(1e-10, 0.3, 300)
        self.xray_energy = xray_energy
        self.ysim = None
        self.z = None
        self.SLDsim = None
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        # make a local copy not to modify the header information
        sample_model = ml.SampleModel.from_dict(self.sample_model.to_dict())

        layers = sample_model.resolve_to_layers()
        self.signals.resolved.emit()

        if refnx is None:
            # refnx is not available, only resolve model
            return

        from refnx.reflect import SLD, ReflectModel, Structure

        if self.xray_energy is not None:
            structure = Structure()
            for lj in layers:
                m = SLD(lj.material.get_sld() * 1e6)
                structure |= m(lj.thickness.as_unit("angstrom"), lj.roughness.as_unit("angstrom"))
            model = ReflectModel(structure, bkg=0.0)
        else:
            structure = Structure()
            for lj in layers:
                m = SLD(lj.material.get_sld(xray_energy=self.xray_energy) * 1e6)
                structure |= m(lj.thickness.as_unit("angstrom"), lj.roughness.as_unit("angstrom"))
            model = ReflectModel(structure, bkg=0.0)

        self.ysim = model(self.x)
        self.z, self.SLDsim = structure.sld_profile()

        self.signals.finished.emit()


class MainWindow(QMainWindow):
    current_model: ml.SampleModel

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()

        self.init_editor()
        self.update_model()

    def init_editor(self):
        doc = self.ui.model_editor.document()
        font = doc.defaultFont()
        font.setFamily("Courier New")
        doc.setDefaultFont(font)
        doc.setPlainText(DEFAULT_MODEL)

    def update_model(self):
        """
        Use the text in the editor to update the model. If an error occurs the editor
        shows a red background and the model stays unchanged.
        """
        sample_yaml = self.ui.model_editor.toPlainText()
        try:
            sample_dict = yaml.safe_load(sample_yaml)
            sample_model = ml.SampleModel.from_dict(sample_dict)
        except Exception as e:
            self.ui.model_editor.setStyleSheet("background-color: #ffaaaa;")
        else:
            self.ui.model_editor.setStyleSheet("background-color: #ffffff;")
            self.current_model = sample_model
            # regenerate the model yaml
            self.ui.model_editor.setPlainText(self.current_model.to_yaml())

        self._worker = SimulationWorker(self.current_model)
        self._worker.signals.finished.connect(self.plot_model)
        self.threadpool.start(self._worker)

        self.update_builder()

    def plot_model(self):
        self.ui.graph_refl.axes.clear()
        self.ui.graph_refl.axes.semilogy(self._worker.x, self._worker.ysim)
        self.ui.graph_refl.axes.set_xlabel("Q / Å$^{-1}$")
        self.ui.graph_refl.axes.set_ylabel("Reflectivity")
        self.ui.graph_refl.fig.draw_idle()
        self.ui.graph_sld.axes.clear()
        self.ui.graph_sld.axes.plot(self._worker.SLDsim, -self._worker.z)
        self.ui.graph_sld.axes.set_xlabel("SLD / 10$^{-6}$ Å$^{-2}$")
        self.ui.graph_sld.axes.set_ylabel("z-depth / Å")
        self.ui.graph_sld.fig.draw_idle()

    def update_builder(self):
        scene = QGraphicsScene(0, 0, 200, 400)

        # rect = QGraphicsRectItem(0, 0, 100, 50)
        #
        # rect.setPos(50, 20)
        #
        # brush = QBrush(Qt.red)
        # rect.setBrush(brush)
        #
        # pen = QPen(Qt.cyan)
        # pen.setWidth(10)
        # rect.setPen(pen)
        #
        # ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
        # ellipse.setPos(75, 30)
        #
        # brush = QBrush(Qt.blue)
        # ellipse.setBrush(brush)
        #
        # pen = QPen(Qt.green)
        # pen.setWidth(5)
        # ellipse.setPen(pen)
        #
        # scene.addItem(ellipse)
        # scene.addItem(rect)
        #
        # ellipse.setFlag(QGraphicsItem.ItemIsMovable)

        self.ui.model_builder.setScene(scene)
