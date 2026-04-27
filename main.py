"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

try:
    file_path = sys.argv[1]
    args = sys.argv[2:]

    tasks = read_todo_file(file_path)

    i = 0
    while i < len(args):

        if args[i] == "view":
            print("Tasks:")
            for t in tasks:
                print(t)
            i += 1

        elif args[i] == "add":
            if i + 1 >= len(args):
                print('Task description required for "add".')
                i += 1
            else:
                tasks.append(args[i + 1])
                print(f'Task "{args[i + 1]}" added.')
                i += 2

        elif args[i] == "remove":
            if i + 1 >= len(args):
                print('Task description required for "remove".')
                i += 1
            else:
                if args[i + 1] in tasks:
                    tasks.remove(args[i + 1])
                    print(f'Task "{args[i + 1]}" removed.')
                else:
                    print(f'Task "{args[i + 1]}" not found.')
                i += 2

        else:
            print("Command not found!")
            break

    write_todo_file(file_path, tasks)

except IndexError:
    print("Insufficient arguments provided!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                