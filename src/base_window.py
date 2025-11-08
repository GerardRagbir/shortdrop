"""
Base window class for the student taxi booking application.
This class provides a reusable parent window that can be extended
by specific windows like Bookings, Drivers, Customers, and Cars.
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QToolBar
)
from PyQt6.QtCore import Qt, QSize
from typing import Optional, List


class BaseWindow(QMainWindow):
    """
    Base window class for the taxi booking application.
    
    Provides:
    - Window title and size management
    - Central widget with layout
    - Button toolbar area
    - Common window functionality
    """
    
    def __init__(self, name: str, size: Optional[QSize] = None, parent=None):
        """
        Initialize the base window.
        
        Args:
            name: Window title/name
            size: Optional window size (defaults to 800x600)
            parent: Optional parent widget
        """
        super().__init__(parent)
        
        # Set window title
        self.setWindowTitle(name)
        
        # Set window size (default to 800x600 if not provided)
        if size is None:
            size = QSize(800, 600)
        self.resize(size)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create toolbar for buttons
        self.toolbar = QToolBar("Main Toolbar")
        self.toolbar.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
        
        # Store buttons for easy access
        self.buttons: List[QPushButton] = []
        
        # Initialize UI components (to be overridden by child classes)
        self._setup_ui()
    
    def _setup_ui(self):
        """
        Setup the UI components.
        Override this method in child classes to add specific UI elements.
        """
        pass
    
    def add_button(
        self, 
        text: str, 
        callback=None, 
        tooltip: str = "",
        add_to_toolbar: bool = True
    ) -> QPushButton:
        """
        Add a button to the window.
        
        Args:
            text: Button text
            callback: Optional callback function to connect to clicked signal
            tooltip: Optional tooltip text
            add_to_toolbar: If True, add to toolbar; if False, add to main layout
            
        Returns:
            The created QPushButton
        """
        button = QPushButton(text)
        
        if tooltip:
            button.setToolTip(tooltip)
        
        if callback:
            button.clicked.connect(callback)
        
        if add_to_toolbar:
            self.toolbar.addWidget(button)
        else:
            self.main_layout.addWidget(button)
        
        self.buttons.append(button)
        return button
    
    def add_widget(self, widget: QWidget):
        """
        Add a widget to the main layout.
        
        Args:
            widget: Widget to add
        """
        self.main_layout.addWidget(widget)
    
    def add_layout(self, layout: QVBoxLayout | QHBoxLayout):
        """
        Add a layout to the main layout.
        
        Args:
            layout: Layout to add
        """
        self.main_layout.addLayout(layout)
    
    def clear_central_widget(self):
        """
        Clear all widgets from the central widget (except toolbar).
        Useful for refreshing the view.
        """
        while self.main_layout.count():
            child = self.main_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def show(self):
        """Override show to ensure window is displayed properly."""
        super().show()

