"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

try:
    file_path = sys.argv[1]
    command = sys.argv[2]

    if command == "view":
        tasks = read_todo_file(file_path)

        print("Tasks:")
        for task in tasks:
            print(task)

    elif command == "add":
        task = sys.argv[3]

        tasks = read_todo_file(file_path)
        tasks.append(task)
        write_todo_file(file_path, tasks)

        print(f'Task "{task}" added.')

    elif command == "remove":
        task = sys.argv[3]

        tasks = read_todo_file(file_path)

        try:
            tasks.remove(task)
            write_todo_file(file_path, tasks)
            print(f'Task "{task}" removed.')
        except ValueError:
            print(f'Task "{task}" not found.')

    else:
        raise ValueError("Command not found!")

except IndexError:
    if len(sys.argv) >= 3:
        command = sys.argv[2]

        if command == "add":
            print('Task description required for "add".')
        elif command == "remove":
            print('Task description required for "remove".')
    else:
        pass

except ValueError as error:
    print(error)