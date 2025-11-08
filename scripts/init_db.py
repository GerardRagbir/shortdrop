"""
Database initialization script for the student taxi booking application.
Creates all necessary tables for bookings, drivers, customers, and cars.
"""

import sys
from pathlib import Path

# Add parent directory to path to import src modules
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from src.database import Database


def init_database(db_name: str = "taxi_booking.db"):
    """
    Initialize the database with all required tables.
    
    Args:
        db_name: Name of the database file
    """
    db = Database(db_name)
    
    try:
        # Create customers table
        db.create_table(
            "customers",
            """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            """
        )
        print("✓ Created 'customers' table")
        
        # Create drivers table
        db.create_table(
            "drivers",
            """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            license_number TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            email TEXT,
            car_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (car_id) REFERENCES cars(id)
            """
        )
        print("✓ Created 'drivers' table")
        
        # Create cars table
        db.create_table(
            "cars",
            """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER,
            license_plate TEXT NOT NULL UNIQUE,
            color TEXT,
            driver_id INTEGER,
            average_rating REAL DEFAULT 0.0,
            total_rides INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (driver_id) REFERENCES drivers(id)
            """
        )
        print("✓ Created 'cars' table")
        
        # Create bookings table
        db.create_table(
            "bookings",
            """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            pickup_location TEXT NOT NULL,
            dropoff_location TEXT NOT NULL,
            pickup_latitude REAL,
            pickup_longitude REAL,
            dropoff_latitude REAL,
            dropoff_longitude REAL,
            booking_date TIMESTAMP NOT NULL,
            status TEXT DEFAULT 'pending',
            fare_amount REAL,
            distance_km REAL,
            duration_minutes INTEGER,
            rating INTEGER,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (driver_id) REFERENCES drivers(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
            """
        )
        print("✓ Created 'bookings' table")
        
        # Create a junction table for bookings with multiple customers (if needed)
        db.create_table(
            "booking_customers",
            """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            UNIQUE(booking_id, customer_id)
            """
        )
        print("✓ Created 'booking_customers' junction table")
        
        # Create indexes for better query performance
        db.execute("CREATE INDEX IF NOT EXISTS idx_bookings_driver_id ON bookings(driver_id)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_bookings_customer_id ON bookings(customer_id)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_drivers_car_id ON drivers(car_id)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_cars_driver_id ON cars(driver_id)")
        print("✓ Created database indexes")
        
        print(f"\n✓ Database '{db_name}' initialized successfully!")
        print(f"  Database location: {db.db_path}")
        
    except Exception as e:
        print(f"✗ Error initializing database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Initialize the taxi booking database")
    parser.add_argument(
        "--db-name",
        type=str,
        default="taxi_booking.db",
        help="Name of the database file (default: taxi_booking.db)"
    )
    
    args = parser.parse_args()
    
    print("Initializing database...")
    print("-" * 50)
    init_database(args.db_name)
    print("-" * 50)

