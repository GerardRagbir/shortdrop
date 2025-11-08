"""
Drivers window for the student taxi booking application.
Shows a list of drivers and their associated cars.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QTextEdit
from PyQt6.QtCore import QSize
from ..base_window import BaseWindow


class DriversWindow(BaseWindow):
    """
    Window for managing drivers.
    Shows list of drivers and their associated cars.
    """
    
    def __init__(self, parent=None):
        super().__init__(
            name="Drivers",
            size=QSize(1000, 600),
            parent=parent
        )
    
    def _setup_ui(self):
        """Setup the drivers UI with list and details."""
        # Create horizontal layout for list and details
        content_layout = QHBoxLayout()
        
        # Left side: List of drivers
        drivers_list_widget = QWidget()
        drivers_layout = QVBoxLayout(drivers_list_widget)
        
        drivers_label = QLabel("Drivers")
        drivers_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        drivers_layout.addWidget(drivers_label)
        
        self.drivers_list = QListWidget()
        self.drivers_list.setMinimumWidth(300)
        self.drivers_list.itemSelectionChanged.connect(self._on_driver_selected)
        drivers_layout.addWidget(self.drivers_list)
        
        content_layout.addWidget(drivers_list_widget)
        
        # Right side: Driver details
        details_widget = QWidget()
        details_layout = QVBoxLayout(details_widget)
        
        details_label = QLabel("Driver Details")
        details_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        details_layout.addWidget(details_label)
        
        self.driver_details = QTextEdit()
        self.driver_details.setReadOnly(True)
        self.driver_details.setPlaceholderText("Select a driver to view details")
        details_layout.addWidget(self.driver_details)
        
        content_layout.addWidget(details_widget)
        
        # Add content layout to main layout
        self.add_layout(content_layout)
        
        # Add action buttons
        self.add_button("Refresh", self._refresh_drivers, "Refresh drivers list")
        self.add_button("Add Driver", self._add_driver, "Add a new driver")
        self.add_button("Edit Driver", self._edit_driver, "Edit selected driver")
    
    def _on_driver_selected(self):
        """Handle driver selection change."""
        current_item = self.drivers_list.currentItem()
        if current_item:
            # TODO: Load driver details from database
            driver_name = current_item.text()
            self.driver_details.setPlainText(
                f"Driver: {driver_name}\n\n"
                "Details will be loaded from database.\n"
                "Will include:\n"
                "- Driver information\n"
                "- Associated cars\n"
                "- Contact details"
            )
    
    def _refresh_drivers(self):
        """Refresh the drivers list."""
        # TODO: Implement database query to refresh drivers
        print("Refreshing drivers...")
    
    def _add_driver(self):
        """Open dialog to add a new driver."""
        # TODO: Implement add driver dialog
        print("Adding new driver...")
    
    def _edit_driver(self):
        """Open dialog to edit the selected driver."""
        # TODO: Implement edit driver dialog
        print("Editing driver...")

