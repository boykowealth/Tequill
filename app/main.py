from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLabel,
    QListWidget, QListWidgetItem, QInputDialog, QMessageBox,
    QSplitter, QFileDialog
)
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

import markdown2
import sys

from style import light_mode
from session import NotebookSession
from manager import NotebookManager
from text import SmartTextEdit

class NotebookWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tequill")
        self.resize(1920, 1080)
        self.move(0, 0)

        self.manager = NotebookManager()
        self.current_session = None
        self.setStyleSheet(light_mode(self))

        ## Central widget
        central = QWidget()
        self.setCentralWidget(central)

        self.list = QListWidget()
        self.editor = SmartTextEdit()
        self.viewer = QWebEngineView()

        ## Left panel (notebook list)
        self.list_panel = QWidget()
        list_layout = QVBoxLayout()
        list_layout.setContentsMargins(5, 5, 5, 5)
        list_layout.setSpacing(5)
        
        # Create a compact label for Notebooks
        notebooks_label = QLabel("Notebooks")
        notebooks_label.setMaximumHeight(20)
        notebooks_label.setStyleSheet("font-size: 12px; font-weight: bold; padding: 2px; margin: 0;")
        
        list_layout.addWidget(notebooks_label)
        list_layout.addWidget(self.list)
        self.list_panel.setLayout(list_layout)

        ## Editor panel
        editor_panel = QWidget()
        editor_layout = QVBoxLayout()
        editor_layout.setContentsMargins(10, 10, 10, 10)
        editor_layout.setSpacing(5)
        
        # Create a compact label for Editor
        editor_label = QLabel("Editor")
        editor_label.setMaximumHeight(20)
        editor_label.setStyleSheet("font-size: 12px; font-weight: bold; padding: 2px; margin: 0;")
        
        editor_layout.addWidget(editor_label)
        editor_layout.addWidget(self.editor)
        editor_panel.setLayout(editor_layout)

        ## Viewer panel
        viewer_panel = QWidget()
        viewer_layout = QVBoxLayout()
        viewer_layout.setContentsMargins(10, 10, 10, 10)
        viewer_layout.setSpacing(5)

        # Create a compact label for Rendered View
        viewer_label = QLabel("Rendered View")
        viewer_label.setMaximumHeight(20)
        viewer_label.setStyleSheet("font-size: 12px; font-weight: bold; padding: 2px; margin: 0;")

        viewer_layout.addWidget(viewer_label)
        viewer_layout.addWidget(self.viewer)
        viewer_panel.setLayout(viewer_layout)

        ## Right side: Editor + Viewer
        self.right_splitter = QSplitter(Qt.Horizontal)
        self.right_splitter.addWidget(editor_panel)
        self.right_splitter.addWidget(viewer_panel)
        self.right_splitter.setSizes([2, 1])

        ## Main splitter: Sidebar + Right panel
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_splitter.addWidget(self.list_panel)
        self.main_splitter.addWidget(self.right_splitter)
        self.main_splitter.setSizes([150, 1000])

        ## Layout setup
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.main_splitter)

        self.create_menu_bar()
        self.load_sessions()
        self.setup_connections()

    def create_menu_bar(self):
        menubar = self.menuBar()

        ## File
        file_menu = menubar.addMenu("File")
        self.new_action = QAction("New", self)
        self.save_action = QAction("Save", self)
        self.rename_action = QAction("Rename", self)
        self.delete_action = QAction("Delete", self)
        file_menu.addActions([self.new_action, self.save_action, self.rename_action, self.delete_action])

        ## View
        view_menu = menubar.addMenu("View")
        self.toggle_sidebar_action = QAction("Toggle Sidebar", self)
        self.render_action = QAction("Render", self)
        view_menu.addActions([self.toggle_sidebar_action, self.render_action])

        ## Export
        export_menu = menubar.addMenu("Export")
        self.export_html_action = QAction("Export HTML", self)
        self.export_pdf_action = QAction("Export PDF", self)
        self.export_md_action = QAction("Export Markdown", self)
        export_menu.addActions([self.export_html_action, self.export_pdf_action, self.export_md_action])

    def setup_connections(self):
        self.new_action.triggered.connect(self.create_new)
        self.save_action.triggered.connect(self.save_current)
        self.rename_action.triggered.connect(self.rename_current)
        self.delete_action.triggered.connect(self.delete_current)
        self.toggle_sidebar_action.triggered.connect(self.toggle_notebook_list)
        self.render_action.triggered.connect(self.render_content)
        self.export_html_action.triggered.connect(self.export_html)
        self.export_pdf_action.triggered.connect(self.export_pdf)
        self.export_md_action.triggered.connect(self.export_markdown)
        self.list.itemClicked.connect(self.load_selected)

    def toggle_notebook_list(self):
        sizes = self.main_splitter.sizes()
        if sizes[0] == 0:
            self.main_splitter.setSizes([150, sizes[1]])
        else:
            self.main_splitter.setSizes([0, sizes[1]])

    def create_new(self):
        self.current_session = NotebookSession()
        self.editor.clear()
        self.viewer.setHtml("")
        self.load_sessions()

    def save_current(self):
        if self.current_session:
            self.current_session.content = self.editor.toPlainText()
            self.manager.save_session(self.current_session)
            self.load_sessions()

    def rename_current(self):
        if not self.current_session:
            return
        title, ok = QInputDialog.getText(self, "Rename Notebook", "Title:", text=self.current_session.title)
        if ok and title:
            self.current_session.title = title
            self.save_current()

    def delete_current(self):
        if not self.current_session:
            return
        confirm = QMessageBox.question(self, "Delete", f"Delete notebook '{self.current_session.title}'?")
        if confirm == QMessageBox.Yes:
            self.manager.delete_session(self.current_session.session_id)
            self.current_session = None
            self.editor.clear()
            self.viewer.setHtml("")
            self.load_sessions()

    def load_sessions(self):
        self.list.clear()
        sessions = self.manager.get_all_sessions()
        for s in sessions:
            item = QListWidgetItem(s.title)
            item.setData(Qt.UserRole, s)
            self.list.addItem(item)

    def load_selected(self, item):
        session = item.data(Qt.UserRole)
        self.current_session = session
        self.editor.setPlainText(session.content)
        self.render_content()

    def render_content(self):
        if not self.current_session:
            return
        content = self.editor.toPlainText()
        html = markdown2.markdown(content)
        template = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: 'Arial', monospace;
                    background-color: #ffffff;
                    color: #333333;
                    padding: 12px;
                    margin: 0;
                    box-sizing: border-box;
                    border: 0px solid #cccccc;
                    border-radius: 6px;
                    max-width: 100%;
                    height: 100%;
                }}
            </style>
            <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
            <script type="text/javascript" id="MathJax-script" async
              src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
            </script>
        </head>
        <body>{html}</body>
        </html>
        """
        self.viewer.setHtml(template)

    def export_html(self):
        if not self.current_session:
            return
        content = self.editor.toPlainText()
        html = markdown2.markdown(content)
        full_html = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
            <script type="text/javascript" id="MathJax-script" async
              src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
            </script>
        </head>
        <body>{html}</body>
        </html>
        """
        path, _ = QFileDialog.getSaveFileName(self, "Export as HTML", f"{self.current_session.title}.html", "HTML Files (*.html)")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(full_html)
            QMessageBox.information(self, "Exported", f"Notebook exported as HTML:\n{path}")

    def export_pdf(self):
        if not self.current_session:
            return
        content = self.editor.toPlainText()
        html = markdown2.markdown(content)
        template = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
            <script type="text/javascript" id="MathJax-script" async
              src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
            </script>
        </head>
        <body>{html}</body>
        </html>
        """
        path, _ = QFileDialog.getSaveFileName(self, "Export as PDF", f"{self.current_session.title}.pdf", "PDF Files (*.pdf)")
        if path:
            def on_pdf_ready(success):
                if success:
                    QMessageBox.information(self, "Exported", f"Notebook exported as PDF:\n{path}")
                else:
                    QMessageBox.warning(self, "Error", "Failed to generate PDF.")
            self.viewer.setHtml(template)
            self.viewer.page().pdfPrintingFinished.connect(on_pdf_ready)
            self.viewer.page().printToPdf(path)

    def export_markdown(self):
        if not self.current_session:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export as Markdown", f"{self.current_session.title}.md", "Markdown Files (*.md)")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())
            QMessageBox.information(self, "Exported", f"Notebook exported as Markdown:\n{path}")


if __name__ == "__main__":
    print("Running instance 1.1 of Tequill, please wait for the display window to appear...")
    app = QApplication(sys.argv)
    window = NotebookWidget()
    window.show()
    sys.exit(app.exec())