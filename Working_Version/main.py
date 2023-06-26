#!/usr/bin/env python3

"""Import SQL Functions And Run Them"""

SQL_Mem = __import__('SQLite').SQL_In_Memory

if __name__ == '__main__':
    SQL_Mem()
