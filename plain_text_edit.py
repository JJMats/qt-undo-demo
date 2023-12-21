from PyQt5 import QtGui
from PyQt5.QtWidgets import QPlainTextEdit, QUndoStack

from undo_commands import UndoCommandPlainTextEdit


class PlainTextEdit(QPlainTextEdit):
    """The PlainTextEdit class overrides the QPlainTextEdit class by providing additional undo/redo control.

    args:
        undo_stack (QUndoStack): A QUndoStack object to push QUndoCommands to

    """

    def __init__(self, undo_stack: QUndoStack):
        super().__init__()
        self.undo_stack = undo_stack
        self.last_text = ""
        self.text_now = ""

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        # Clear any background color changes
        self.setStyleSheet("QLineEdit {background-color: #FFFFFF;}")

        # Save the state of the control by storing the text
        self.last_text = self.toPlainText()

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        # Store the current text
        self.text_now = self.toPlainText()

        # Compare the current text to the text when we entered the control
        if self.text_now != self.last_text:
            # Set the background color of the text area to red if a change has been detected
            self.setStyleSheet("QPlainTextEdit {background-color: #FF0000;}")

            # Push an undo command onto the undostack
            cmd = UndoCommandPlainTextEdit(self, self.last_text, self.text_now, "Updated Plain Text Contents")
            self.undo_stack.push(cmd)
        else:
            self.setStyleSheet("QPlainTextEdit {background-color: #00FF00;}")
