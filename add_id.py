import sqlite3

def add_id_to_table(table_name):
    # Create a temporary table with the id column
    cursor.execute(f"""
        CREATE TABLE {table_name}_temp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT
        );
    """)

    # Copy data from the original table to the temporary one
    cursor.execute(f"INSERT INTO {table_name}_temp (exercise) SELECT exercise FROM {table_name};")

    # Drop the original table
    cursor.execute(f"DROP TABLE {table_name};")

    # Rename the temporary table to the original table name
    cursor.execute(f"ALTER TABLE {table_name}_temp RENAME TO {table_name};")

conn = sqlite3.connect('exercise_db.db')
cursor = conn.cursor()

tables = [
    "Closures",
    "Comprehension",
    "Data_types",
    "Dictionaries",
    "Exceptions",
    "Indexing_and_Slicing",
    "Lists",
    "Local_and_global_scope",
    "Methods_of_types",
    "Mutable_and_Imutable_types",
    "Sets",
    "Short_circuit_evaluation",
    "String_manipulation",
    "Tuples"
]

for table in tables:
    add_id_to_table(table)

conn.commit()
conn.close()
