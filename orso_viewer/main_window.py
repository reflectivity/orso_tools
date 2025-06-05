from orsopy import fileio
from orsopy.fileio import model_language
from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, Signal, Slot
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem

from orso_viewer.ui_main_window import Ui_MainWindow

try:
    import refnx
except ImportError:
    refnx = None


class WorkerSignals(QObject):
    finished = Signal()


class SimulationWorker(QRunnable):
    """Thread to analyze a sample model in the background."""

    def __init__(self, sample_model: model_language.SampleModel, x, xray_energy=None):
        super(SimulationWorker, self).__init__()
        self.sample_model = sample_model
        self.x = x
        self.xray_energy = xray_energy
        self.ysim = None
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        """Your long-running job goes in this method."""
        print("Thread start")
        # make a local copy not to modify the header information
        sample_model = model_language.SampleModel.from_dict(self.sample_model.to_dict())

        from refnx.reflect import SLD, ReflectModel, Structure

        layers = sample_model.resolve_to_layers()

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

        self.signals.finished.emit()


class MainWindow(QMainWindow):
    datasets: list[fileio.OrsoDataset]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.datasets = []
        self.threadpool = QThreadPool()

        self.ui.header_tree.setColumnCount(2)
        self.ui.header_tree.setHeaderLabels(["Key", "Type"])

    def read_file(self, filename):
        self.datasets = fileio.load_orso(filename)

        self.ui.dataset_list.clear()
        self.ui.dataset_list.addItems([str(di.info.data_set) for di in self.datasets])

        self.ui.dataset_list.setCurrentRow(0)

    @Slot(int)
    def dataset_selected(self, index):
        self.plot_dataset(index)
        self.update_header(index)

    def plot_dataset(self, index):
        dataset = self.datasets[index]
        sc = self.ui.data_plot
        sc.axes.clear()
        sc.axes.errorbar(dataset.data[:, 0], dataset.data[:, 1], dataset.data[:, 2], label="data")
        sc.axes.set_yscale("log")
        sc.axes.set_xlabel(dataset.info.columns[0].name + " / " + (dataset.info.columns[0].unit or ""))
        sc.axes.set_ylabel(dataset.info.columns[1].name + " / " + (dataset.info.columns[1].unit or "1"))

        try:
            sample_model = dataset.info.data_source.sample.model
        except AttributeError:
            pass
        else:
            if refnx is not None:
                self.worker = SimulationWorker(sample_model, dataset.data[:, 0])
                self.worker.signals.finished.connect(self.plot_simulation)
                self.threadpool.start(self.worker)

    @Slot()
    def plot_simulation(self):
        worker = self.worker
        x = worker.x
        ysim = worker.ysim
        sc = self.ui.data_plot
        sc.axes.semilogy(x, ysim, label="model")
        sc.axes.legend()
        sc.draw()

    def update_header(self, index):
        tv = self.ui.header_tree
        dataset: fileio.OrsoDataset = self.datasets[index]
        data = dataset.info.to_dict()
        items = []
        for key, value in data.items():
            obj = getattr(dataset.info, key)
            item = QTreeWidgetItem([key, obj.__class__.__name__])
            item.setData(0, Qt.ItemDataRole.UserRole, obj)
            # ext = str(value)
            # child = QTreeWidgetItem([value, ext])
            # item.addChild(child)
            items.append(item)

        tv.insertTopLevelItems(0, items)
