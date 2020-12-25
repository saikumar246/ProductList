list=[]
def read():
    fp=open("product.txt","r")
    list=fp.readlines()
    fp.close()
    list.sort() #load the list into an ascending linear list.
    for i in range(len(list)):
        t=list[i]
        if t[-1]=='\n':
            list[i]=t[:-1]
    return list
def insert(list):
    a=str(input("Ente the product to insert into the list:"))
    list.append(a)
    list.sort()
    return list
def delete(list):
    b=str(input("Enter the product to delete from the list:"))
    list.remove(b)
    list.sort()
    return list

def savefile(list):
    fp1=open("product.txt","w")
    for i in range(len(list)):
        list[i]=list[i]+'\n'
    fp1.writelines(list)



def main():
    while(1):
        print("1. Read the list from the text file")
        print("2. Insert new product")
        print("3. Delete the product from the list")
        print("4. Exit")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            list=read()
            print(list)
        elif(choice==2):
            list=insert(list)
            print("list after insert:",list)
        elif(choice==3):
            list=delete(list)
            print("List after delete:",list)
        elif(choice==4):
            savefile(list)
            exit()
        else:
            print("Enter a valid choice:")



if __name__=="__main__":
    main()