import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, \
    QStatusBar, QUndoStack, QWidget, QLineEdit, QUndoView, QUndoGroup, QPushButton

from plain_text_edit import PlainTextEdit

undo_group = QUndoGroup()


class MainWindow(QMainWindow):
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

        self.status_bar = QStatusBar()
        # self.status_bar.setStatusTip("My status tip!")  # this shows when you hover over the window
        self.setStatusBar(self.status_bar)

        self.content = MainContent(self.undo_stack)
        central_widget = self.content
        self.setCentralWidget(central_widget)
        self.show()

    def create_actions(self):
        # self.undo_button = QPushButton()
        # self.undo_action = self.undo_button.clicked
        # self.undo_action = self.undo_stack.createUndoAction(self.toolbar)
        self.undo_action = undo_group.createUndoAction(self.toolbar)
        # self.undo_action.setIcon(getIcon("undo.svg"))
        self.undo_action.setShortcut("Ctrl+z")
        self.undo_action.setText("Undo")
        # self.undo_action.connect

        # TODO: Override the undo shortcut and change the undo action to a button
        #       Then, use the undo button clicked event to set focus to the button (if necessary), and then perform the
        #       undo operation?

        # self.redo_action = self.undo_stack.createRedoAction(self.toolbar)
        self.redo_action = undo_group.createRedoAction(self.toolbar)
        self.redo_action.setShortcut("Ctrl+y")
        self.redo_action.setText("Redo")
        # self.redo_action.setShortcut(QKeySequence.)

        self.toolbar.addAction(self.undo_action)
        self.toolbar.addAction(self.redo_action)

        self.push_button = QPushButton()
        self.push_button.setText("My Button")
        self.toolbar.addWidget(self.push_button)

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

        self.undo_button = QPushButton()
        self.undo_button.setText("Undo")
        self.undo_button.setShortcut("Ctrl+b")
        self.toolbar.addWidget(self.undo_button)
        self.undo_button.clicked.connect(self.undo_click_handler)

        self.redo_button = QPushButton()
        self.redo_button.setText("Redo")
        self.redo_button.setShortcut("Ctrl+v")
        self.toolbar.addWidget(self.redo_button)
        self.redo_button.clicked.connect(self.redo_click_handler)

        # self.undo_stack.undo()

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

    def undo_click_handler(self):
        self.setFocus()
        self.do_undo()

    def redo_click_handler(self):
        self.setFocus()
        self.do_redo()

    def do_undo(self):
        self.undo_stack.undo()

    def do_redo(self):
        self.undo_stack.redo()


class MainContent(QWidget):
    def __init__(self, undo_stack: QUndoStack):
        super().__init__()
        vbox = QVBoxLayout()

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter line edit text...")

        # line_edit.setStatusTip(f"Undo available: {line_edit.isUndoAvailable()}")
        vbox.addWidget(self.line_edit)

        # self.plain_text = QPlainTextEdit()
        self.plain_text = PlainTextEdit(undo_stack)
        self.plain_text.setPlaceholderText("Enter text here...")
        # self.plain_text.focusInEvent()
        self.plain_text.setUndoRedoEnabled(False)
        # undo_group.addStack(plain_text)
        # plain_text.setStatusTip(f"Undo available: {plain_text.undoAvailable}")
        vbox.addWidget(self.plain_text)

        self.button = QPushButton()
        self.button.setText("Click me!")
        vbox.addWidget(self.button)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = MainWindow()
undo_group.addStack(window.undo_stack)
# undo_group.addStack(window.content.plain_text.document().UndoStack)
undo_group.setActiveStack(window.undo_stack)
sys.exit(app.exec_())
