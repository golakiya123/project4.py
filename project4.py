data=[]

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

def stats():
    return min(data),max(data),sum(data),sum(data)/len(data)

print("Welcome to the Data Analyzer and Transformer Program")
while True:

    print("\nMain Menu:")
    print("1 Input Data")
    print("2 Display Data Summary")
    print("3 Calculate Factorial")
    print("4 Filter Data by Threshold")
    print("5 Sort Data")
    print("6 Display Dataset Statistics")
    print("7 Exit Program")

    ch=int(input("\n Please enter your choice: "))

    if ch==1:
        data=list(map(int,input("Enter data: ").split()))
        print("Data entered successfully")

    elif ch==2:
        print("\nData Summary:")
        print("Total elements:",len(data))
        print("Minimum value:",min(data))
        print("Maximum value:",max(data))
        print("Sum of all values:",sum(data))
        print("Average value:",round(sum(data)/len(data),2))

    elif ch==3:
        n=int(input("Enter a number to calculate its factorial: "))
        print("Factorial of",n,"is:",fact(n))

    elif ch==4:
        t=int(input("Enter threshold value: "))
        print("Filtered Data:",[x for x in data if x>=t])

    elif ch==5:
        s=int(input("1. Ascending\n2. Descending\nEnter choice: "))
        print("Sorted Data:",sorted(data,reverse=s==2))

    elif ch==6:
        a,b,c,d=stats()
        print("\nDataset Statistics:")
        print("Minimum value:",a)
        print("Maximum value:",b)
        print("Sum of all values:",c)
        print("Average value:",round(d,2))

    elif ch==7:
        print("Thank you for using the Data Analyzer and Transformer Program.Goodbye!")
        break

    
