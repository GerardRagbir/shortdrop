# import required modules to get application setup
import sys
from pathlib import Path

# needed for access to QtCore functions
from PyQt6.QtWidgets import QApplication

# Import the main window from the src package
from src.views import MainWindow

        
# main function to run the application
if __name__ == "__main__":
    # Check if database exists, if not initialize it
    root_dir = Path(__file__).parent
    db_file = root_dir / "taxi_booking.db"
    
    if not db_file.exists():
        print("Database not found. Initializing database...")
        try:
            from scripts.init_db import init_database
            init_database()
            print("Database initialized successfully!\n")
        except Exception as e:
            print(f"Error initializing database: {e}")
            sys.exit(1)
    
    # create a new application
    app = QApplication(sys.argv)
    # create a new main window
    window = MainWindow()
    # show the window
    window.show()
    # run the application
    sys.exit(app.exec()) # exit the application
    