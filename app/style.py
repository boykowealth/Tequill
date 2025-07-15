def light_mode(self):
    return """
    QWidget {
        background-color: #f8f8f8 ;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333333;
    }

    QLabel {
        font-size: 15px;
        font-weight: 600;
        color: #111111;
        padding: 6px 12px;
    }

    QListWidget {
        background-color: #FAFAFA;
        border: none;
        border-radius: 12px;
        padding: 0;
        outline: none;
    }

    QListWidget::item {
        padding: 14px 16px;
        border-bottom: 1px solid #E5E7EB;
        font-size: 14px;
        color: #222222;
        margin-left: 8px;
        margin-right: 8px;
    }

    QListWidget::item:selected {
        background-color: #D0E7FF;
        color: #0B60D8;
        border-radius: 10px;
        margin: 4px 8px;
    }

    QTextEdit {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 16px;
        font-size: 16px;
        color: #111111;
        outline: none;
        selection-background-color: #D0E7FF;
    }

    QSplitter::handle {
        background-color: #E5E7EB;
        width: 4px;
        margin: 0 4px;
        border-radius: 2px;
    }

    QScrollBar:vertical {
        background: transparent;
        width: 8px;
        margin: 0px 0px 0px 0px;
    }

    QScrollBar::handle:vertical {
        background: #A3BFFA;
        min-height: 30px;
        border-radius: 4px;
    }

    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        height: 0px;
    }

    QPushButton {
    background-color: #0078d4;
    color: #ffffff;
    border: none;
    border-radius: 20px; /* half or more of the button height */
    padding: 10px 30px; /* vertical padding controls height, horizontal for width */
    min-height: 20px;   /* fixed height for consistent rounding */
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.6px;
    }

    QPushButton:hover {
        background-color: #005ea6;
    }

    QPushButton:pressed {
        background-color: #004477;
    }

        QMenuBar {
        background-color: #f9f9f9;
        color: #333;
        padding: 4px;
        spacing: 3px;
    }

    QMenuBar::item {
        background: transparent;
        padding: 4px 12px;
        margin: 0 2px;
    }

    QMenuBar::item:selected {
        background: #d0e0ff;  /* Highlight on hover */
        border-radius: 4px;
    }

    QMenu {
        background-color: #ffffff;
        border: 1px solid #ccc;
        padding: 4px;
    }

    QMenu::item {
        background-color: transparent;
        padding: 6px 20px;
        margin: 2px;
    }

    QMenu::item:selected {
        background-color: #d0e0ff;  /* Highlight on hover */
        color: black;
        border-radius: 4px;
    }
    """