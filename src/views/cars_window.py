"""
Cars window for the student taxi booking application.
Shows a registered list of cars with last rides and average rating.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QTextEdit
from PyQt6.QtCore import QSize
from ..base_window import BaseWindow


class CarsWindow(BaseWindow):
    """
    Window for managing cars.
    Shows registered list of cars, last rides, and average rating.
    """
    
    def __init__(self, parent=None):
        super().__init__(
            name="Cars",
            size=QSize(1000, 600),
            parent=parent
        )
    
    def _setup_ui(self):
        """Setup the cars UI with list and details."""
        # Create horizontal layout for list and details
        content_layout = QHBoxLayout()
        
        # Left side: List of cars
        cars_list_widget = QWidget()
        cars_layout = QVBoxLayout(cars_list_widget)
        
        cars_label = QLabel("Registered Cars")
        cars_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        cars_layout.addWidget(cars_label)
        
        self.cars_list = QListWidget()
        self.cars_list.setMinimumWidth(300)
        self.cars_list.itemSelectionChanged.connect(self._on_car_selected)
        cars_layout.addWidget(self.cars_list)
        
        content_layout.addWidget(cars_list_widget)
        
        # Right side: Car details
        details_widget = QWidget()
        details_layout = QVBoxLayout(details_widget)
        
        details_label = QLabel("Car Details")
        details_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        details_layout.addWidget(details_label)
        
        self.car_details = QTextEdit()
        self.car_details.setReadOnly(True)
        self.car_details.setPlaceholderText("Select a car to view details")
        details_layout.addWidget(self.car_details)
        
        content_layout.addWidget(details_widget)
        
        # Add content layout to main layout
        self.add_layout(content_layout)
        
        # Add action buttons
        self.add_button("Refresh", self._refresh_cars, "Refresh cars list")
        self.add_button("Add Car", self._add_car, "Register a new car")
        self.add_button("Edit Car", self._edit_car, "Edit selected car")
    
    def _on_car_selected(self):
        """Handle car selection change."""
        current_item = self.cars_list.currentItem()
        if current_item:
            # TODO: Load car details from database
            car_name = current_item.text()
            self.car_details.setPlainText(
                f"Car: {car_name}\n\n"
                "Details will be loaded from database.\n"
                "Will include:\n"
                "- Car information (make, model, year)\n"
                "- Registration details\n"
                "- Last rides\n"
                "- Average rating\n"
                "- Associated driver"
            )
    
    def _refresh_cars(self):
        """Refresh the cars list."""
        # TODO: Implement database query to refresh cars
        print("Refreshing cars...")
    
    def _add_car(self):
        """Open dialog to register a new car."""
        # TODO: Implement add car dialog
        print("Adding new car...")
    
    def _edit_car(self):
        """Open dialog to edit the selected car."""
        # TODO: Implement edit car dialog
        print("Editing car...")

