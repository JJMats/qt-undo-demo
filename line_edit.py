from PyQt5 import QtGui
from PyQt5.QtWidgets import QLineEdit, QUndoStack

from undo_commands import UndoCommandLineEdit


class LineEdit(QLineEdit):
    """The LineEdit class overrides the QLineEdit class by providing additional undo/redo control.

    args:
        undo_stack (QUndoStack): A QUndoStack object to push QUndoCommands to
    """

    def __init__(self, undo_stack: QUndoStack):
        super().__init__()
        self.undo_stack = undo_stack
        self.last_text = ""
        self.text_now = ""

    def undo(self):
        # Ignore the default undo behavior
        pass

    def redo(self):
        # Ignore the default redo behavior
        pass

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        # Clear any background color changes
        self.setStyleSheet("QLineEdit {background-color: #FFFFFF;}")

        # Save the state of the control by storing the text
        self.last_text = self.text()

        # Set the text of the control to itself to clear the Undo/Redo stack that is built into the control
        super().setText(self.text())

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        # Store the current text
        self.text_now = self.text()

        # Compare the current text to the text when we entered the control
        if self.text_now != self.last_text:
            # Set the background color of the text area to red if a change has been detected
            self.setStyleSheet("QLineEdit {background-color: #FF0000;}")

            # Push an undo command onto the undostack
            cmd = UndoCommandLineEdit(self, self.last_text, self.text_now, "Updated Line Edit Contents")
            self.undo_stack.push(cmd)
        else:
            # Set the background color of the text area to green if the text has not changed
            self.setStyleSheet("QLineEdit {background-color: #00FF00;}")
