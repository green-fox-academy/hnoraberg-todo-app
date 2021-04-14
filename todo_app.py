import sys
import os


if len(sys.argv) == 1:
    print("\nCommand Line Todo application"
          "\n\n============================= \n\nCommand line arguments: \n"
          " -l   Lists all the tasks \n -a   Adds a new task \n"
          " -r   Removes a task \n -c   Completes a task")

elif len(sys.argv) > 1:

    if sys.argv[1] == "-l":
        count = 1
        with open('todo.txt') as listingTodo:
            filesize = os.path.getsize("todo.txt")
            if filesize == 0:
                print("No todos for today! :)")
            else:
                for lines in listingTodo:
                    if "[X] " in lines:
                        print(str(count) + " - " + lines)
                        count += 1
                    else:
                        print(str(count) + " - [ ] " + lines)
                        count += 1

    elif sys.argv[1] == "-a":
        if len(sys.argv) < 3:
            print("Unable to add: no task provided")
        else:
            with open("todo.txt", "a") as addingTodo:
                addingTodo.write(sys.argv[2] + "\n")

    elif sys.argv[1] == "-r":
        if len(sys.argv) < 3:
            print("Unable to remove: no index provided")
        elif len(sys.argv) == 3:
            index = int(sys.argv[2]) - 1
            with open("todo.txt", "r+") as removingTodo:
                lines = removingTodo.readlines()
                del lines[index]
                removingTodo.seek(0)
                removingTodo.truncate()
                removingTodo.writelines(lines)

    elif sys.argv[1] == "-c":
        if len(sys.argv) < 3:
            print("Unable to check: no index provided")
        elif len(sys.argv) == 3:
            index = int(sys.argv[2]) - 1
            with open("todo.txt", "r+") as checkingTodo:
                elements = checkingTodo.readlines(index)
                elements.insert(index, "[X] ")
                checkingTodo.seek(0)
                checkingTodo.writelines(elements)

    else:
        print("Unsupported argument \n\nCommand line arguments: \n"
          " -l   Lists all the tasks \n -a   Adds a new task \n"
          " -r   Removes a task \n -c   Completes a task")