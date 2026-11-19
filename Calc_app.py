 

def cal():
    operation=int(input())
    return operation
def add():
    a=int(input())
    b=int(input())
    print(a+b)

def sub():
    a=int(input())
    b=int(input())
    print(a-b)

def mul():
    a=int(input())
    b=int(input())
    print(a*b)

def div():
    a=int(input())
    b=int(input())
    print(a/b)

while True:
    print("""
          ====CALCULATOR====
          1 - ADDITION
          2 - SUBSTRACTION
          3 - MULTIPLICATION
          4 - DIVISION
          0 - EXIT(/)
          """)
    res=cal()
    
    if res==1:
        add()
    elif res==2:
        sub()
    elif res==3:
        mul()
    elif res==4:
        div()
    elif res==0:
        break
    else:
        print("Invalid choice")


         
    
        
    
    
    
