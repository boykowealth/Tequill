from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QKeyEvent, QTextCursor
from PySide6.QtCore import Qt


class SmartTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            '"': '"',
            "'": "'",
            '*': '*',
            '_': '_',
            '`': '`'
        }

    def keyPressEvent(self, event: QKeyEvent):
        key = event.text()
        cursor = self.textCursor()

        if key in self.pairs:
            closing = self.pairs[key]
            if cursor.hasSelection():
                selected = cursor.selectedText()
                cursor.insertText(f"{key}{selected}{closing}")
            else:
                cursor.insertText(f"{key}{closing}")
                cursor.movePosition(QTextCursor.Left)
                self.setTextCursor(cursor)
            return

        super().keyPressEvent(event)