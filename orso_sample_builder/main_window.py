from traceback import format_exc

import yaml

from numpy import linspace
from orsopy.fileio import model_language as ml
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from PySide6.QtWidgets import QErrorMessage, QMainWindow, QToolButton

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
    exception = Signal(str)


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

        try:
            layers = sample_model.resolve_to_layers()
        except Exception as e:
            self.show_message(f"Could not resolve model to layers:\n{format_exc()}")
            return
        self.signals.resolved.emit()

        if refnx is None:
            # refnx is not available, only resolve model
            return

        from refnx.reflect import SLD, ReflectModel, Structure

        if self.xray_energy is not None:
            structure = Structure()
            for lj in layers:
                try:
                    m = SLD(lj.material.get_sld() * 1e6)
                except Exception as e:
                    self.show_message(f"Could not resolve material for layer {lj}:\n{e}")
                    return
                structure |= m(lj.thickness.as_unit("angstrom"), lj.roughness.as_unit("angstrom"))
            model = ReflectModel(structure, bkg=0.0)
        else:
            structure = Structure()
            for lj in layers:
                try:
                    m = SLD(lj.material.get_sld(xray_energy=self.xray_energy) * 1e6)
                except Exception as e:
                    self.show_message(f"Could not resolve material for layer {lj}:\n{e}")
                    return
                structure |= m(lj.thickness.as_unit("angstrom"), lj.roughness.as_unit("angstrom"))
            model = ReflectModel(structure, bkg=0.0)

        self.ysim = model(self.x)
        self.z, self.SLDsim = structure.sld_profile()

        self.signals.finished.emit()

    def show_message(self, message):
        self.signals.exception.emit(message)


class MainWindow(QMainWindow):
    current_model: ml.SampleModel

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()

        self.init_editor()

    def init_editor(self):
        doc = self.ui.model_editor.document()
        font = doc.defaultFont()
        font.setFamily("Courier New")
        doc.setDefaultFont(font)
        for chld in self.ui.editor_toolbar.children():
            if isinstance(chld, QToolButton):
                chld.pressed.connect(self.insert_class)
        from orsopy.fileio import model_language as ml

        for subcls in ml.SubStackType.__subclasses__():
            if subcls is ml.SubStack:
                continue
            self.ui.complex_selector.addItem(subcls.__name__)
        self.ui.complex_selector.currentIndexChanged.connect(self.insert_complex)

        # doc.setPlainText(DEFAULT_MODEL)
        doc.setPlainText("")
        self.current_model = ml.SampleModel(stack="vacuum | Fe 100 | Si")
        self.ui.model_editor.insert_class("SampleModel", **self.current_model.to_dict())

    def show_error(self, message):
        dia = QErrorMessage()
        dia.showMessage("<pre>" + message + "</pre")
        dia.exec()

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
        self._worker.signals.resolved.connect(self.show_model)
        self._worker.signals.finished.connect(self.plot_model)
        self._worker.signals.exception.connect(self.show_error)
        self.threadpool.start(self._worker)
        self.ui.model_viewer.preparing_sample()

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

    def show_model(self):
        self.ui.model_viewer.show_sample_model(self._worker.sample_model)

    def insert_class(self):
        self.ui.model_editor.insert_class(self.sender().text())

    def insert_complex(self, idx):
        if idx == 0:
            return
        self.ui.complex_selector.setCurrentIndex(0)
        self.ui.model_editor.insert_class(self.ui.complex_selector.itemText(idx))
