from PyQt5 import QtGui
from PyQt5.QtWidgets import QPlainTextEdit, QUndoStack

from undo_commands import UndoCommandPlainTextEdit


class PlainTextEdit(QPlainTextEdit):
    def __init__(self, undo_stack: QUndoStack):
        super().__init__()
        self.undo_stack = undo_stack
        self.last_text = ""
        self.text_now = ""

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        self.setStyleSheet("QPlainTextEdit {background-color: #00FFFF;}")
        self.last_text = self.toPlainText()

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        # self.setStyleSheet("QPlainTextEdit {background-color: #FFFFFF;}")
        self.text_now = self.toPlainText()
        if self.text_now != self.last_text:
            self.setStyleSheet("QPlainTextEdit {background-color: #FF0000;}")
            cmd = UndoCommandPlainTextEdit(self, self.text_now, self.last_text, "Updated Plain Text Contents")
            self.undo_stack.push(cmd)
        else:
            self.setStyleSheet("QPlainTextEdit {background-color: #00FF00;}")

    def hasFocus(self) -> bool:
        return super().hasFocus
        super().focus
