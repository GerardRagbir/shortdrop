"""
Database layer for the student taxi booking application.
Uses SQLite3 for data persistence.
"""

import sqlite3
import os
from typing import Optional, List, Dict, Any, Tuple
from pathlib import Path

# CRUD
# Create, Read (One, Many, All), Update, Delete


class Database:
    """
    Database class for handling SQLite operations.
    Provides CRUD methods for database interactions.
    """
    
    def __init__(self, db_name: str = "taxi_booking.db"):
        """
        Initialize the database connection.
        
        Args:
            db_name: Name of the database file (default: taxi_booking.db)
        """
        # Get the root directory (parent of src)
        root_dir = Path(__file__).parent.parent
        self.db_path = root_dir / db_name
        self.connection: Optional[sqlite3.Connection] = None
        self._connect()
    
    def _connect(self):
        """Establish connection to the database."""
        try:
            self.connection = sqlite3.connect(str(self.db_path))
            self.connection.row_factory = sqlite3.Row  # Return rows as dictionaries
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise
    
    def _ensure_connection(self):
        """Ensure database connection is active."""
        if self.connection is None:
            self._connect()
        try:
            self.connection.execute("SELECT 1")
        except sqlite3.Error:
            self._connect()
    
    def execute(
        self, 
        query: str, 
        params: Optional[Tuple] = None
    ) -> sqlite3.Cursor:
        """
        Execute a SQL query.
        
        Args:
            query: SQL query string
            params: Optional tuple of parameters for parameterized queries
            
        Returns:
            Cursor object
        """
        self._ensure_connection()
        try:
            if params:
                cursor = self.connection.execute(query, params)
            else:
                cursor = self.connection.execute(query)
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            self.connection.rollback()
            print(f"Error executing query: {e}")
            raise
    
    def executemany(
        self, 
        query: str, 
        params_list: List[Tuple]
    ) -> sqlite3.Cursor:
        """
        Execute a SQL query multiple times with different parameters.
        
        Args:
            query: SQL query string
            params_list: List of parameter tuples
            
        Returns:
            Cursor object
        """
        self._ensure_connection()
        try:
            cursor = self.connection.executemany(query, params_list)
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            self.connection.rollback()
            print(f"Error executing query: {e}")
            raise
    
    def create(
        self, 
        table: str, 
        data: Dict[str, Any]
    ) -> int:
        """
        Create a new record in the specified table.
        
        Args:
            table: Table name
            data: Dictionary of column names and values
            
        Returns:
            ID of the created record
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        params = tuple(data.values())
        
        cursor = self.execute(query, params)
        return cursor.lastrowid
    
    def read_all(
        self, 
        table: str, 
        conditions: Optional[Dict[str, Any]] = None,
        order_by: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Read all records from the specified table.
        
        Args:
            table: Table name
            conditions: Optional dictionary of column:value pairs for WHERE clause
            order_by: Optional ORDER BY clause (e.g., "id DESC")
            
        Returns:
            List of dictionaries representing rows
        """
        query = f"SELECT * FROM {table}"
        params = None
        
        if conditions:
            where_clause = ' AND '.join([f"{key} = ?" for key in conditions.keys()])
            query += f" WHERE {where_clause}"
            params = tuple(conditions.values())
        
        if order_by:
            query += f" ORDER BY {order_by}"
        
        cursor = self.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def read_one(
        self, 
        table: str, 
        record_id: Optional[int] = None,
        conditions: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Read a single record from the specified table.
        
        Args:
            table: Table name
            record_id: Optional ID of the record (uses 'id' column)
            conditions: Optional dictionary of column:value pairs for WHERE clause
            
        Returns:
            Dictionary representing the row, or None if not found
        """
        query = f"SELECT * FROM {table}"
        params = None
        
        if record_id is not None:
            query += " WHERE id = ?"
            params = (record_id,)
        elif conditions:
            where_clause = ' AND '.join([f"{key} = ?" for key in conditions.keys()])
            query += f" WHERE {where_clause}"
            params = tuple(conditions.values())
        else:
            raise ValueError("Either record_id or conditions must be provided")
        
        query += " LIMIT 1"
        
        cursor = self.execute(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def update(
        self, 
        table: str, 
        record_id: int, 
        data: Dict[str, Any]
    ) -> bool:
        """
        Update a record in the specified table.
        
        Args:
            table: Table name
            record_id: ID of the record to update
            data: Dictionary of column names and new values
            
        Returns:
            True if update was successful, False otherwise
        """
        if not data:
            return False
        
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE id = ?"
        params = tuple(data.values()) + (record_id,)
        
        cursor = self.execute(query, params)
        return cursor.rowcount > 0
    
    def delete(
        self, 
        table: str, 
        record_id: int
    ) -> bool:
        """
        Delete a record from the specified table.
        
        Args:
            table: Table name
            record_id: ID of the record to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        query = f"DELETE FROM {table} WHERE id = ?"
        params = (record_id,)
        
        cursor = self.execute(query, params)
        return cursor.rowcount > 0
    
    def create_table(self, table_name: str, schema: str):
        """
        Create a table with the specified schema.
        
        Args:
            table_name: Name of the table to create
            schema: SQL CREATE TABLE statement (without CREATE TABLE table_name)
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        self.execute(query)
    
    def table_exists(self, table_name: str) -> bool:
        """
        Check if a table exists in the database.
        
        Args:
            table_name: Name of the table to check
            
        Returns:
            True if table exists, False otherwise
        """
        query = """
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name=?
        """
        cursor = self.execute(query, (table_name,))
        return cursor.fetchone() is not None
    
    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

