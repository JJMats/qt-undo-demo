from PyQt5.QtWidgets import QUndoCommand, QPlainTextEdit, QLineEdit


class UndoCommandPlainTextEdit(QUndoCommand):
    """The UndoCommandPlainTextEdit class creates a QUndoCommand object for the QPlainTextEdit control.

    args:
        control (QPlainTextEdit): A reference to the QPlainTextEdit control
        text_before (str): The original text string
        text_after (str): The new text string
        description (str): A descriptive string of the event for the undo history
    """

    def __init__(self, control: QPlainTextEdit, text_before: str, text_after: str, description: str):
        super().__init__(description)
        self._control = control
        self._text_before = text_before
        self._text_after = text_after

    def undo(self) -> None:
        self._control.setPlainText(self._text_before)

    def redo(self) -> None:
        self._control.setPlainText(self._text_after)


class UndoCommandLineEdit(QUndoCommand):
    """The UndoCommandLineEdit class creates a QUndoCommand object for the QLineEdit control.

    args:
        control (UndoCommandLineEdit): A reference to the UndoCommandLineEdit control
        text_before (str): The original text string
        text_after (str): The new text string
        description (str): A descriptive string of the event for the undo history
    """

    def __init__(self, control: QLineEdit, text_before: str, text_after: str, description: str):
        super().__init__(description)
        self._control = control
        self._text_before = text_before
        self._text_after = text_after

    def undo(self) -> None:
        self._control.setText(self._text_before)

    def redo(self) -> None:
        self._control.setText(self._text_after)
