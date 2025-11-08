"""
Main window for the student taxi booking application.
Provides navigation between different windows.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QSize, Qt
from ..base_window import BaseWindow
from .bookings_window import BookingsWindow
from .drivers_window import DriversWindow
from .customers_window import CustomersWindow
from .cars_window import CarsWindow


class MainWindow(BaseWindow):
    """
    Main navigation window for the taxi booking application.
    """
    
    def __init__(self, parent=None):
        super().__init__(
            name="Student Taxi Booking - Main Menu",
            size=QSize(600, 400),
            parent=parent
        )
        
        # Store child windows
        self.bookings_window = None
        self.drivers_window = None
        self.customers_window = None
        self.cars_window = None
    
    def _setup_ui(self):
        """Setup the main menu UI."""
        # Welcome label
        welcome_label = QLabel("Welcome to Student Taxi Booking System")
        welcome_label.setStyleSheet("font-size: 20px; font-weight: bold; padding: 20px;")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_widget(welcome_label)
        
        # Navigation buttons
        nav_layout = QVBoxLayout()
        nav_layout.setSpacing(15)
        
        # Bookings button
        bookings_btn = QPushButton("Bookings")
        bookings_btn.setMinimumHeight(50)
        bookings_btn.clicked.connect(self._open_bookings)
        nav_layout.addWidget(bookings_btn)
        
        # Drivers button
        drivers_btn = QPushButton("Drivers")
        drivers_btn.setMinimumHeight(50)
        drivers_btn.clicked.connect(self._open_drivers)
        nav_layout.addWidget(drivers_btn)
        
        # Customers button
        customers_btn = QPushButton("Customers")
        customers_btn.setMinimumHeight(50)
        customers_btn.clicked.connect(self._open_customers)
        nav_layout.addWidget(customers_btn)
        
        # Cars button
        cars_btn = QPushButton("Cars")
        cars_btn.setMinimumHeight(50)
        cars_btn.clicked.connect(self._open_cars)
        nav_layout.addWidget(cars_btn)
        
        # Add navigation layout
        nav_widget = QWidget()
        nav_widget.setLayout(nav_layout)
        self.add_widget(nav_widget)
    
    def _open_bookings(self):
        """Open the bookings window."""
        if self.bookings_window is None:
            self.bookings_window = BookingsWindow()
        self.bookings_window.show()
    
    def _open_drivers(self):
        """Open the drivers window."""
        if self.drivers_window is None:
            self.drivers_window = DriversWindow()
        self.drivers_window.show()
    
    def _open_customers(self):
        """Open the customers window."""
        if self.customers_window is None:
            self.customers_window = CustomersWindow()
        self.customers_window.show()
    
    def _open_cars(self):
        """Open the cars window."""
        if self.cars_window is None:
            self.cars_window = CarsWindow()
        self.cars_window.show()

