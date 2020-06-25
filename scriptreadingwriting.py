# fh = open("example.txt","w")
fh = open('/home/sudip/Dilip/python A to z learning/examplel/examplell.txt ',"w")

# fh.write("the task involved infile is good file manipulation reading from data file.\n")
#
# fh.write("the task involved infile is good file manipulation reading from data file.")

for i in range(1,11):
    fh.write("Line : %d  \n"%i)
fh.close()