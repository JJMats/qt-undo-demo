import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QVBoxLayout, QMainWindow, \
    QStatusBar, QUndoStack, QWidget, QLineEdit, QUndoView


# undo_group = QUndoGroup()


# class Window(QWidget):
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Plain Text Edit"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.undo_stack = QUndoStack()
        # undo_group.addStack(self.undo_stack)

        self.create_toolbar()
        self.create_actions()
        self.init_window()
        self.create_undo_view()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # vbox = QVBoxLayout()
        # plain_text = QPlainTextEdit()
        # plain_text.setPlaceholderText("Enter text here...")

        self.status_bar = QStatusBar()
        # self.status_bar.setStatusTip("My status tip!")  # this shows when you hover over the window
        self.setStatusBar(self.status_bar)
        # plain_text.setUndoRedoEnabled(False)

        # vbox.addWidget(self.toolbar)
        # vbox.addWidget(plain_text)
        # self.setLayout(vbox)

        # self.setCentralWidget(vbox)
        # dock_widget = QDockWidget()
        # dock_widget.addAction(plain_text)
        # self.setCentralWidget(dock_widget)

        central_widget = MainContent()
        self.setCentralWidget(central_widget)

        self.show()

    def create_actions(self):
        self.undo_action = self.undo_stack.createUndoAction(self.toolbar)
        # self.undo_action = undo_group.createUndoAction(self.toolbar)
        # self.undo_action.setIcon(getIcon("undo.svg"))
        self.undo_action.setShortcut("Ctrl+z")
        self.undo_action.setText("Undo")

        self.redo_action = self.undo_stack.createRedoAction(self.toolbar)
        # self.redo_action = undo_group.createRedoAction(self.toolbar)
        self.redo_action.setShortcut("Ctrl+y")
        self.redo_action.setText("Redo")
        # self.redo_action.setShortcut(QKeySequence.)

        self.toolbar.addAction(self.undo_action)
        self.toolbar.addAction(self.redo_action)

    def create_undo_view(self):
        # self.undo_view = QUndoView(undo_group)
        self.undo_view = QUndoView(self.undo_stack)
        self.undo_view.setWindowTitle("Undo Command List")
        self.undo_view.show()
        # self.undo_view.setAttribute(WA_QuitOnClose, false)

    def create_toolbar(self):
        # self.toolbar = QToolBar()
        # self.window.addToolBar("My Toolbar")
        self.toolbar = self.addToolBar("My Toolbar")
        # self.toolbar = self.window().addToolBar()
        # self.toolbar = self.addToolBar("QT Demo")

        # self.undo_action = QAction(QtGui.QIcon("undo.svg"), "Undo", self)
        # self.undo_action.setShortcut("Ctrl+Z")
        # self.toolbar.addAction(self.undo_action)

        # self.undo_action = self.undo_stack.createUndoAction(self.toolbar)
        # # self.undo_action = undo_group.createUndoAction(self.toolbar)
        # # self.undo_action.setIcon(getIcon("undo.svg"))
        # self.undo_action.setShortcut("Ctrl+z")
        # self.undo_action.setText("Undo")

        # self.redo_action = QAction(QtGui.QIcon("redo.svg"), "Redo", self)
        # self.redo_action.setShortcut("Ctrl+Y")
        # self.toolbar.addAction(self.redo_action)

        # self.redo_action = self.undo_stack.createRedoAction(self.toolbar)
        # # self.redo_action = undo_group.createRedoAction(self.toolbar)
        # self.redo_action.setShortcut("Ctrl+y")
        # self.redo_action.setText("Redo")

        # self.toolbar.addAction(self.undo_action)
        # self.toolbar.addAction(self.redo_action)

        # self.undo_button = QToolButton()
        #
        # self.toolbar.addWidget(self.undo_button)
        #
        # self.redo_button = QToolButton()
        # self.toolbar.addWidget(self.redo_button)

    # def init_actions(self):
    #     self.undoAction =
    #     self.undoAction.setShortcut("Ctrl+Z")


class MainContent(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()

        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter line edit text...")
        # line_edit.setStatusTip(f"Undo available: {line_edit.isUndoAvailable()}")
        vbox.addWidget(line_edit)

        plain_text = QPlainTextEdit()
        plain_text.setPlaceholderText("Enter text here...")
        # undo_group.addStack(plain_text)
        # plain_text.setStatusTip(f"Undo available: {plain_text.undoAvailable}")
        vbox.addWidget(plain_text)

        self.setLayout(vbox)
        # self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
