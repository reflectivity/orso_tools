from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat, QTextCursor
from PySide6.QtWidgets import QTextEdit


class OrsoSampleHighlighter(QSyntaxHighlighter):
    _orso_special = ["stack"]

    def __init__(self, parent=None):
        super(OrsoSampleHighlighter, self).__init__(parent)
        self.dict_key_format = QTextCharFormat()
        self.dict_key_format.setFontWeight(QFont.Bold)
        self.dict_key_format.setForeground(Qt.GlobalColor.darkMagenta)
        self.special_key_format = QTextCharFormat()
        self.special_key_format.setFontWeight(QFont.Bold)
        self.special_key_format.setForeground(Qt.GlobalColor.darkGreen)
        self.stack_format = QTextCharFormat()
        self.stack_format.setFontWeight(QFont.Bold)
        self.stack_format.setForeground(Qt.GlobalColor.black)

    def highlightBlock(self, text):
        expression = QRegularExpression("\\b[a-zA-Z_]*:")
        i = expression.globalMatch(text)
        while i.hasNext():
            match = i.next()
            name = match.capturedTexts()[0][:-1]
            if name in self._orso_special:
                self.setFormat(match.capturedStart(), match.capturedLength(), self.special_key_format)
            else:
                self.setFormat(match.capturedStart(), match.capturedLength(), self.dict_key_format)

        expression = QRegularExpression("(?<=stack:).*")
        i = expression.globalMatch(text)
        while i.hasNext():
            match = i.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), self.stack_format)


class ModelEditor(QTextEdit):

    def __init__(self, parent):
        QTextEdit.__init__(self, parent)
        self.highlighter = OrsoSampleHighlighter(self.document())

    def keyPressEvent(self, event):
        tab_char = "  "  # could be anything including spaces
        if event.key() == Qt.Key_Backtab:
            # get current cursor
            cur = self.textCursor()
            cur.clearSelection()

            # move to begining of line and select text to first word
            cur.movePosition(QTextCursor.StartOfLine)
            cur.movePosition(QTextCursor.NextWord, QTextCursor.KeepAnchor)
            sel_text = cur.selectedText()

            # if the text starts with the tab_char, replace it
            if sel_text.startswith(tab_char):
                text = sel_text.replace(tab_char, "", 1)
                cur.insertText(text)
        elif event.key() == Qt.Key_Tab:
            # get current cursor
            cur = self.textCursor()
            cur.clearSelection()

            # move to begining of line and select text to first word
            cur.movePosition(QTextCursor.StartOfLine)
            cur.insertText(tab_char)
            cur.movePosition(QTextCursor.NextWord, QTextCursor.KeepAnchor)

        else:
            return QTextEdit.keyPressEvent(self, event)
