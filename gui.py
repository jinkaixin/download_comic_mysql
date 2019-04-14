import tkinter as tk
from tkinter.filedialog import askdirectory



class Get_info():
    def __init__(self):
        self.url=''
        self.folder_path=''
        self.window = tk.Tk()
        self.window.title('漫画下载器')
        self.url_receive = tk.StringVar()
        self.folder_path_receive = tk.StringVar()
        tk.Label(self.window,text='请输入漫画网址').grid(row=0,column=0)
        tk.Label(self.window,text='存储路径').grid(row=1,column=0)
        tk.Entry(self.window,width=50,textvariable=self.url_receive,show=None).grid(row=0,column=1)
        tk.Entry(self.window,width=50,textvariable=self.folder_path_receive,show=None).grid(row=1,column=1)
        tk.Button(self.window,text='选择存储路径',command=self.select_path).grid(row=1,column=2)
        tk.Button(self.window,text='开始下载',command=self.update_info).grid(row=3,column=2)
        self.window.mainloop()
        
    def update_info(self):
        self.url=self.url_receive.get()
        self.folder_path = self.folder_path_receive.get()
        if self.url != '' and self.folder_path != '':
            self.window.destroy()
    
    def select_path(self):
        self.folder_path_receive.set(askdirectory())
        

class Choose_chapter():
    def __init__(self,chapter_list):
        self.choosed_chapter_list = []
        self.chapter_list = chapter_list
        self.window = tk.Tk()
        self.window.title('请选择需要下载的章节')
        self.listbox = tk.Listbox(self.window,selectmode=tk.MULTIPLE,width=60,height=20)
        for chapter in self.chapter_list:
            self.listbox.insert(tk.END,chapter)
        self.sc = tk.Scrollbar(self.window)
        self.listbox.config(yscrollcommand=self.sc.set)
        self.sc.config(command=self.listbox.yview)
        
        self.listbox.grid(row=0,column=0)
        self.sc.grid(row=0,column=1,sticky=tk.N+tk.S)
        tk.Button(self.window,text='下载全部',command=self.all_chapters).grid(row=1,column=2,sticky=tk.W+tk.E)
        tk.Label(self.window,text='').grid(row=2,column=2,sticky=tk.W+tk.E)
        tk.Button(self.window,text='只下载选定的章节',command=self.choosed_chapter).grid(row=3,column=2,sticky=tk.W+tk.E)
        self.window.mainloop()
        
    def choosed_chapter(self):
        for num in self.listbox.curselection():
            self.choosed_chapter_list.append(self.listbox.get(num))
        if len(self.choosed_chapter_list) > 0:
            self.window.destroy()
    
    def all_chapters(self):
        self.choosed_chapter_list = self.chapter_list
        self.window.destroy()



