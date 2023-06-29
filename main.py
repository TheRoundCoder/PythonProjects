user_prompt = "Enter a Task: "

todo_list = []
while True:
    user_action = input("Type add or show: ")

    match user_action:
        case 'add':
                todo = input("Enter a task: ")
                todo_list.append(todo.capitalize())
        # | <---- bitwise or Operator
        case 'show' | 'display':
                for task in todo_list:
                      print(task)
        case 'close':
                exit()
        #when entering gibberish
        case _:
                print("Wrong command")asdasdasd









## For-loops & Match-case
