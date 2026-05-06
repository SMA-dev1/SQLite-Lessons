# import sqlite3
# from contextlib import closing
#
#
# # CRUD
# def get_connection(database_path):
#     return closing(sqlite3.connect(database_path))
#
# def create_employee(database_path,employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id):
#     with get_connection(database_path) as connection:
#         cursor = connection.cursor()
#         cursor.execute("INSERT INTO employees (employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id) VALUES (?, ?,?,?, ?,?,?, ?,?,?)", (employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id))
#         connection.commit()
#         return cursor.lastrowid
#
#
# def get_employee(database_path, employee_id):
#     with get_connection(database_path) as connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
#         return cursor.fetchone()
#
#
# def update_employee(database_path, employee_id, first_name,):
#     with get_connection(database_path) as connection:
#         cursor = connection.cursor()
#         if first_name:
#             cursor.execute("UPDATE employees SET first_name=? WHERE employee_id=?", (first_name, employee_id))
#             connection.commit()
#             return "Updated successfully"
#
#
# def delete_employee(database_path, employee_id):
#     with get_connection(database_path) as connection:
#         cursor = connection.cursor()
#         cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
#         connection.commit()
#
# database_path = "sample-database.db"
#
# employee_get = get_employee(database_path,113)
# print(employee_get)
#
# # employee_create = create_employee(database_path,207,"Ali","Valiyev","ali@gmail.com","+998931234567","08-08-2018", 5,1500,3,10)
# # print(employee_create)
#
# employee_update = update_employee(database_path, 126, 'Anvarbek')
# print(employee_update)


# import sqlite3
# from abc import ABC, abstractmethod
# from contextlib import closing
#
#
# class BaseCRUD(ABC):
#     def __init__(self, database_path,jobs):
#         self.database_path = database_path
#         self.jobs = jobs
#
#     def get_connection(self):
#         return closing(sqlite3.connect(self.database_path))
#
#     def insert(self, **kwargs):
#         with self.get_connection() as connection:
#             cursor = connection.cursor()
#             columns = ', '.join(kwargs.keys())
#             placeholders = ', '.join('?' for _ in kwargs)
#             query = f"INSERT INTO {self.jobs} ({columns}) VALUES ({placeholders})"
#             cursor.execute(query, tuple(kwargs.values()))
#             connection.commit()
#             return cursor.lastrowid
#
#     def get(self, id, job_id="id"):
#         with self.get_connection() as connection:
#             cursor = connection.cursor()
#             query = f"SELECT * FROM {self.jobs} WHERE {job_id}=?"
#             cursor.execute(query, (id,))
#             return cursor.fetchone()
#
#     def update(self, id, job_id="id", **kwargs):
#         with self.get_connection() as connection:
#             cursor = connection.cursor()
#             columns = ', '.join(f"{key}=?" for key in kwargs)
#             query = f"UPDATE {self.jobs} SET {columns} WHERE {job_id}=?"
#             cursor.execute(query, (*kwargs.values(), id))
#             connection.commit()
#
#     def delete(self, id, job_id="id"):
#         with self.get_connection() as connection:
#             cursor = connection.cursor()
#             query = f"DELETE FROM {self.jobs} WHERE {job_id}=?"
#             cursor.execute(query, (id,))
#             connection.commit()
