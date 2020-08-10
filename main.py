from os import walk
from os.path import join,normcase
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import askyesno,showerror
class find():
    def __init__(self) :
        self.root=Tk()
        self.searched=False
        self.searched2=False
        self.root.title("File Finder")
        Label(self.root,text="Select a Folder to search").pack()
        Button(self.root,text="Select",command=self.select_directory).pack()
        self.root.mainloop()
    def search(self):
        file_name=self.e.get()
        self.searched=True
        #print(file_name,"full")
        for dir_name,dir,file in walk(self.directory):
            # print("hi")
            
            for file_ in file:
                # print(dir_name,dir,file,"\n\n")
                if  file_name==file_:
                    # print(file_,"file_")
                    #print(dir,"dir")
                    #print(dir_name,"dir_name")
                    
                        #print("if")
                    full=normcase(join(dir_name,file_))
                    
                    askopenfilename(initialdir=full)
                    self.e.delete(0,END)
                    self.e.insert(0,full)
                    return None
            # elif file_name==file:
            #     print(dir,file)

        
        if self.searched2:
            showerror("Not Found","No Such Directory or file found in selected directory")
        else:
            a=askyesno("Not Found","No Such File In Selected Directory \n Whant to check wether it is a Folder")
            if a:
                self.search2()            
         

    def search2(self):
        file_name=self.e.get()
        self.searched2=True
        #print(file_name,"full")
        for dir_name,dir,file in walk(self.directory):
            
            for file_ in file:
                # print(dir_name,dir,file,"\n\n")
                if  file_name in dir:
                    # print(file_,"file_")
                    #print(dir,"dir")
                    #print(dir_name,"dir_name")
                    
                        #print("if")
                    index=dir.index(file_name)
                    full=normcase(join(dir_name,dir[index]))
                    
                    askopenfilename(initialdir=full)
                    self.e.delete(0,END)
                    self.e.insert(0,full)
                    return None
            # elif file_name==file:
            #     print(dir,file)

        # Label(self.root,text="No Such Folder In Selected Directory \nCan check for file").pack()    
        # Button(self.root,text="check",command=self.search).pack()
        if self.searched:
            showerror("Not Found","No Such Directory or file found in selected directory")
        else:
            a=askyesno("Not Found","No Such Folder In Selected Directory \n Whant to check wether it is a file")
            if a:
                self.search()
    def select_directory(self):
        self.directory=askdirectory(initial="/",title="Select the directory")
        if len(self.directory)>1:
            Label(self.root,text="ENter What You Want to find")
            self.e=Entry(self.root)
            self.e.pack()
            self.searched=False
            self.searched2=False
            Button(self.root,text="Find Folder",command=self.search2).pack()
            Button(self.root,text="Find File",command=self.search).pack()    
            

if __name__ == "__main__":
    find()     


    # f.write(str(file))


