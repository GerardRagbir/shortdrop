"""
Bookings window for the student taxi booking application.
Shows a list of bookings with driver and associated customers,
and displays a simple map.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel
from PyQt6.QtCore import QSize, Qt
from ..base_window import BaseWindow


class BookingsWindow(BaseWindow):
    """
    Window for managing bookings.
    Shows list of bookings with driver and customers, plus a map view.
    """
    
    def __init__(self, parent=None):
        super().__init__(
            name="Bookings",
            size=QSize(1200, 700),
            parent=parent
        )
    
    def _setup_ui(self):
        """Setup the bookings UI with list and map."""
        # Create horizontal layout for list and map
        content_layout = QHBoxLayout()
        
        # Left side: List of bookings
        bookings_list_widget = QWidget()
        bookings_layout = QVBoxLayout(bookings_list_widget)
        
        bookings_label = QLabel("Bookings")
        bookings_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        bookings_layout.addWidget(bookings_label)
        
        self.bookings_list = QListWidget()
        self.bookings_list.setMinimumWidth(400)
        bookings_layout.addWidget(self.bookings_list)
        
        content_layout.addWidget(bookings_list_widget)
        
        # Right side: Map placeholder
        map_widget = QWidget()
        map_layout = QVBoxLayout(map_widget)
        
        map_label = QLabel("Map View")
        map_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        map_layout.addWidget(map_label)
        
        self.map_placeholder = QLabel("Map will be displayed here")
        self.map_placeholder.setStyleSheet(
            "background-color: #f0f0f0; "
            "border: 1px solid #ccc; "
            "min-height: 500px;"
        )
        self.map_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        map_layout.addWidget(self.map_placeholder)
        
        content_layout.addWidget(map_widget)
        
        # Add content layout to main layout
        self.add_layout(content_layout)
        
        # Add action buttons
        self.add_button("Refresh", self._refresh_bookings, "Refresh bookings list")
        self.add_button("New Booking", self._new_booking, "Create a new booking")
    
    def _refresh_bookings(self):
        """Refresh the bookings list."""
        # TODO: Implement database query to refresh bookings
        print("Refreshing bookings...")
    
    def _new_booking(self):
        """Open dialog to create a new booking."""
        # TODO: Implement new booking dialog
        print("Creating new booking...")

