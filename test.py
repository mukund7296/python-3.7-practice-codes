def main():
    f=open("textfile.txt",'w+')
    for i in range(1,101):
        f.write("this is line :"+str(i)+"\n")
    f.close()

if __name__ == '__main__':
    main()
    print("Sucessfully inserted")
