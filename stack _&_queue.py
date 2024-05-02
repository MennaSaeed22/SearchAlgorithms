q = []
s = []
while True:
    print("Enter 1 for stack\nEnter 2 for queue")
    x = int(input())
       #FILO(stack)
       #FIFO(queue)
    if x == 1:
        while True:
          print("Enter 1 for push\n"
                "Enter 2 for pop\n"
                "Enter 3 for print stack\n"
                "Enter 4 for Exit")
          y = int(input())
          if y == 1:
            num = int(input("Enter a number : "))
            s.append(num)
          elif y == 2:
              if s == []:
                  print("stack is empty!\n")
              else:
                  s.pop()
          elif y == 3:
            print(s)
          else :
             break
    else:
        while True:
           print("Enter 1 for enqueue\n"
                 "Enter 2 for dequeue\n"
                 "Enter 3 for print queue\n"
                 "Enter 4 for Exit")
           y = int(input())
           if y == 1:
               num = int(input("Enter a number : "))
               q.append(num)
           elif y == 2:
               if q == []:
                   print("queue is empty!\n")
               else:
                   q.pop(0)
           elif y == 3:
               print(q)
           else:
              break