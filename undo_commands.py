from PyQt5.QtWidgets import QUndoCommand, QPlainTextEdit


class UndoCommandPlainTextEdit(QUndoCommand):
    def __init__(self, control: QPlainTextEdit, text_before: str, text_after: str, description: str):
        super().__init__(description)
        self._control = control
        self._text_before = text_before
        self._text_after = text_after

    def undo(self) -> None:
        self._control.setPlainText(self._text_before)

    def redo(self) -> None:
        self._control.setPlainText(self._text_after)
