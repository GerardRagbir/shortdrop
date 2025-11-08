"""
Customers window for the student taxi booking application.
Shows a list of customers on the left and customer details on the right.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QTextEdit
from PyQt6.QtCore import QSize
from ..base_window import BaseWindow


class CustomersWindow(BaseWindow):
    """
    Window for managing customers.
    Shows list of customers on left and details on right when selected.
    """
    
    def __init__(self, parent=None):
        super().__init__(
            name="Customers",
            size=QSize(1000, 600),
            parent=parent
        )
    
    def _setup_ui(self):
        """Setup the customers UI with list and details."""
        # Create horizontal layout for list and details
        content_layout = QHBoxLayout()
        
        # Left side: List of customers
        customers_list_widget = QWidget()
        customers_layout = QVBoxLayout(customers_list_widget)
        
        customers_label = QLabel("Customers")
        customers_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        customers_layout.addWidget(customers_label)
        
        self.customers_list = QListWidget()
        self.customers_list.setMinimumWidth(300)
        self.customers_list.itemSelectionChanged.connect(self._on_customer_selected)
        customers_layout.addWidget(self.customers_list)
        
        content_layout.addWidget(customers_list_widget)
        
        # Right side: Customer details
        details_widget = QWidget()
        details_layout = QVBoxLayout(details_widget)
        
        details_label = QLabel("Customer Details")
        details_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        details_layout.addWidget(details_label)
        
        self.customer_details = QTextEdit()
        self.customer_details.setReadOnly(True)
        self.customer_details.setPlaceholderText("Select a customer to view details")
        details_layout.addWidget(self.customer_details)
        
        content_layout.addWidget(details_widget)
        
        # Add content layout to main layout
        self.add_layout(content_layout)
        
        # Add action buttons
        self.add_button("Refresh", self._refresh_customers, "Refresh customers list")
        self.add_button("Add Customer", self._add_customer, "Add a new customer")
        self.add_button("Edit Customer", self._edit_customer, "Edit selected customer")
    
    def _on_customer_selected(self):
        """Handle customer selection change."""
        current_item = self.customers_list.currentItem()
        if current_item:
            # TODO: Load customer details from database
            customer_name = current_item.text()
            self.customer_details.setPlainText(
                f"Customer: {customer_name}\n\n"
                "Details will be loaded from database.\n"
                "Will include:\n"
                "- Personal information\n"
                "- Contact details\n"
                "- Booking history\n"
                "- Payment information"
            )
    
    def _refresh_customers(self):
        """Refresh the customers list."""
        # TODO: Implement database query to refresh customers
        print("Refreshing customers...")
    
    def _add_customer(self):
        """Open dialog to add a new customer."""
        # TODO: Implement add customer dialog
        print("Adding new customer...")
    
    def _edit_customer(self):
        """Open dialog to edit the selected customer."""
        # TODO: Implement edit customer dialog
        print("Editing customer...")

