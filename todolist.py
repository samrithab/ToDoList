from stack import *

class InvalidIndexError(Exception):
    pass

class ToDoList:

    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, i):
        self.tasks.pop(i)
    def __len__(self):
        return len(self.tasks)
    def __str__(self):
        s = ""
        for i in range(1, (len(self.tasks)+1)):
            s = s + '{} : {} \n'.format(i, self.tasks[i-1])
        return s

    # ADD IN METHODS HERE ACCORDING TO INSTRUCTIONS #

commands = Stack()
redos = Stack()
todolist = ToDoList()

print("Welcome to your temporary To Do List")
print("-------------------------------------")
print("At any point, you may type: \n" \
            "'v' to view whole list \n" \
            "'d' to delete an existing item \n" \
            "'u' to undo what you just added, \n"
            "'r' to redo what you previously undid)")
print("-------------------------------------")

while True:
    c = input("What is something you need to get done? \n")
    if (c == 'v'):
        print(todolist)
    elif (c == 'd'):
        # MODIFY THIS ACCORDING TO INSTRUCTIONS #
        num = int(input("Delete which task?"))
        try:
            e = todolist.tasks[num - 1]
            todolist.delete_task(num-1)
            print(todolist)
            commands.push(('delete', e, num-1))
        except IndexError:
            print ("The index is invalid")
    elif (c == 'u'):
        try:
            a = commands.pop()
            redos.push(a)
            if a[0] == 'delete':
                b = a[1]
                c = a[2]
                todolist.tasks.insert(c, b)
            else:
               todolist.tasks.pop()
        except IndexError:
            print ("Undo operation is not possible at this point")
        

     # YOUR CODE HERE #
        
    elif (c == 'r'):
        try:
            a = redos.pop()
            b = a[1]
            c = a[2]
            if a[0] == 'delete':
                todolist.tasks.pop(c)
            else:
                todolist.tasks.insert(c, b)
        except IndexError:
            print ("Redo operation is not possible at this point")
        # YOUR CODE HERE #
        
    else:
        todolist.add_task(c)
        commands.push(('insert', c, len(todolist)-1))
        #redos = Stack()
