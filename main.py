import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, \
    QStatusBar, QUndoStack, QWidget, QUndoView, QPushButton

from line_edit import LineEdit
from plain_text_edit import PlainTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 UndoStack Demo"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.undo_stack = QUndoStack()
        self.create_toolbar()
        self.init_window()
        self.create_undo_view()

    def init_window(self):
        """Initializes the window object."""
        # self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Instantiate the status bar object
        self.status_bar = QStatusBar()
        # self.status_bar.setStatusTip("My status tip!")  # this shows when you hover over the window
        self.setStatusBar(self.status_bar)

        # Create the central widget
        self.content = MainContent(self.undo_stack)
        central_widget = self.content
        self.setCentralWidget(central_widget)
        self.show()

    def create_undo_view(self):
        """Creates a view with a list of all the undo_stack contents"""
        self.undo_view = QUndoView(self.undo_stack)
        self.undo_view.setWindowTitle("Undo Command List")
        self.undo_view.show()

    def create_toolbar(self):
        """Creates a toolbar with undo/redo buttons."""
        self.toolbar = self.addToolBar("My Toolbar")

        # Create the undo button
        self.undo_button = QPushButton()
        self.undo_button.setText("Undo")
        self.undo_button.setShortcut("Ctrl+b")
        self.toolbar.addWidget(self.undo_button)
        self.undo_button.clicked.connect(self.undo_click_handler)

        # Create the redo button
        self.redo_button = QPushButton()
        self.redo_button.setText("Redo")
        self.redo_button.setShortcut("Ctrl+v")
        self.toolbar.addWidget(self.redo_button)
        self.redo_button.clicked.connect(self.redo_click_handler)

    def undo_click_handler(self):
        # TODO: Figure out how to remove the cursor from the text areas when the focus is removed
        self.setFocus()
        self.do_undo()

    def redo_click_handler(self):
        # TODO: Figure out how to remove the cursor from the text areas when the focus is removed
        self.setFocus()
        self.do_redo()

    def do_undo(self):
        self.undo_stack.undo()

    def do_redo(self):
        self.undo_stack.redo()


class MainContent(QWidget):
    """The MainContent class defines the layout and controls of the main window."""

    def __init__(self, undo_stack: QUndoStack):
        super().__init__()

        # Use a VBox layout object
        vbox = QVBoxLayout()

        # Create the LineEdit object
        self.line_edit = LineEdit(undo_stack)
        self.line_edit.setPlaceholderText("Enter line edit text...")
        vbox.addWidget(self.line_edit)

        # Create the PlainTextEdit object
        self.plain_text = PlainTextEdit(undo_stack)
        self.plain_text.setPlaceholderText("Enter text here...")
        self.plain_text.setUndoRedoEnabled(False)  # Disable the default undo/redo functionality
        vbox.addWidget(self.plain_text)

        # Create a PushButton object
        self.button = QPushButton()
        self.button.setText("Click me!")
        vbox.addWidget(self.button)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
