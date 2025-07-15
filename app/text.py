from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class AutoCloseTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            '"': '"',
            "'": "'"
        }

    def keyPressEvent(self, event: QKeyEvent):
        key = event.text()
        cursor = self.textCursor()

        if key in self.pairs:
            closing_char = self.pairs[key]
            cursor.insertText(key + closing_char)
            cursor.movePosition(cursor.Left)
            self.setTextCursor(cursor)
        elif key in self.pairs.values():
            # Optional: skip over the closing character if it's already there
            next_char = self.toPlainText()[cursor.position():cursor.position() + 1]
            if next_char == key:
                cursor.movePosition(cursor.Right)
                self.setTextCursor(cursor)
            else:
                super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)
