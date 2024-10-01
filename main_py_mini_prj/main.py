from tkinter import *
from tkinter import ttk,filedialog,messagebox
import os,shutil
import json

#=================================== Plese provide the absolute path ==============================================================================
#================================  path of the extension files (folder in extension_files) =======================================================
path_imagefile = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\extension_files\image.txt"
path_audiofile = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\extension_files\audio.txt"
path_videofile = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\extension_files\video.txt"
path_docfile = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\extension_files\doc.txt"
#=============================================================================================================================================

#====================================== path for images in GUI (folder in prj_pics) ========================================================
path_iconimage = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\icon.ico"
path_logo_icon = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\folder.png"
path_image_icon = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\image.png"
path_audio_icon = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\audio.png"
path_video_icon = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\videos.png"
path_document_icon = r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\documents.png"
path_other_icon =r"C:\Users\Prathamesh Maharnur\Desktop\main_py_mini_prj\prj_pics\other.png"
#======================================================================================================================

class Sorting_App:
    def __init__(self,root):
        self.root = root
        self.root.title("Files Sorting Application")
        self.root.geometry("1600x800+0+0")
        self.root.config(bg = 'white')
        self.root.iconbitmap(path_iconimage)
        self.Frame1 = None
        # self.Frame2 = None
        self.logo_icon=PhotoImage(file = path_logo_icon)
        title = Label(self.root, text = "Files Sorting App", padx = 10,  image = self.logo_icon, compound = LEFT, font = ("impact",40), bg = "#023548", fg = "white", anchor = "w")
        title.place(x = 0, y = 0, relwidth = 1)
        
        #=================================================  function definition to read extension file stored in list (JSON Format) ===================================================
        def add_imageext():
            try:
                with open(path_imagefile, "r") as f:
                    data = json.load(f)
                    return data
                
            except Exception as e:
                print(e)
        def add_videoext():
            try:
                with open(path_videofile, "r") as f:
                    data = json.load(f)
                    return data
                
            except Exception as e:
                print(e)

        def add_audioext():
            try:
                with open(path_audiofile, "r") as f:
                    data = json.load(f)
                    return data
                
            except Exception as e:
                print(e)

        def add_docext():
            try:
                with open(path_docfile, "r") as f:
                    data = json.load(f)
                    return data
                
            except Exception as e:
                print(e)

  
        #================================================ Section 1 ==============================================================================================================================================================================================================================

        self.var_foldername = StringVar()
        lbl_select_folder =  Label(self.root, text = "Select Folder", font = ("times new roman", 25), bg ="white").place(x = 100, y = 100)
        txt_folder_name = Entry(self.root, textvariable = self.var_foldername, font = ("times new roman", 15), state = "readonly", bg = "lightyellow")
        txt_folder_name.place(x = 300, y = 100, height = 40, width = 800)

        btn_browse = Button(self.root, command = self.browse_function, text = "BROWSE", font = ("times new roman", 15, "bold"), bg = "#262626", fg = "white", activebackground = "#262626", cursor = "hand2", activeforeground = "white")
        btn_browse.place(x = 1150, y = 95, height =  45, width = 150)

        hr = Label(self.root, bg = "lightgrey").place(x = 40, y = 160, height = 2, width = 1300)
        vr = Label(self.root, bg = "lightgrey").place(x = 1370, y = 76, height = 720, width = 2)

        self.lbl_setting = Label(self.root, text = "More Options", font = ("times new roman", 15, "bold"), bg ="white", fg = "green")
        self.lbl_setting.place(x = 1390, y = 76)

         #============================================ Section 2 ================================================================================================================
         #========================================= All Extensions ==============================================================================================================
        
        # extension functions are called to assign it to below variables
        self.image_extensions = add_imageext()
        self.audio_extensions = add_audioext()
        self.video_extensions = add_videoext()
        self.doc_extensions = add_docext()
        self.folders = {
                'videos':self.video_extensions,
                'audios':self.audio_extensions,
                'images':self.image_extensions,
                'documents':self.doc_extensions,
            }
        
        # folders_list is defined to avoid recursive creation of folders and sorting for folders named videos, images,....others
        self.folders_list =['videos', 'audios', 'images', 'documents', 'others']

        lbl_select_ext =  Label(self.root, text = "Various Supported Extensions", font = ("times new roman", 20), bg ="white")
        lbl_select_ext.place(x = 50, y = 170)

        self.image_box = ttk.Combobox(self.root, values = self.image_extensions, font = ("times new roman", 15), state = "readonly", justify = CENTER)
        self.image_box.place(x = 60, y = 230, width = 270, height = 35)
        self.image_box.current(0)

        self.video_box = ttk.Combobox(self.root, values = self.video_extensions, font = ("times new roman", 15), state = "readonly", justify = CENTER)
        self.video_box.place(x = 390, y = 230, width = 270, height = 35)
        self.video_box.current(0)

        self.audio_box = ttk.Combobox(self.root, values = self.audio_extensions, font = ("times new roman", 15), state = "readonly", justify = CENTER)
        self.audio_box.place(x = 730, y = 230, width = 270, height = 35)
        self.audio_box.current(0)

        self.doc_box = ttk.Combobox(self.root, values = self.doc_extensions, font = ("times new roman", 15), state = "readonly", justify = CENTER)
        self.doc_box.place(x = 1060, y = 230, width = 270, height = 35)
        self.doc_box.current(0)

        #============================================== Section 3 =======================================================================================
        #============================================== All Image Icons =================================================================================

        self.image_icon = PhotoImage(file = path_image_icon)
        self.audio_icon=PhotoImage(file = path_audio_icon)
        self.video_icon=PhotoImage(file = path_video_icon )
        self.document_icon=PhotoImage(file = path_document_icon)
        self.other_icon=PhotoImage(file = path_other_icon)

        self.Frame1 = Frame(self.root, bd = 2, relief = RIDGE)
        self.Frame1.place(x= 50, y = 300, width = 1300, height = 300)
        self.lbl_total_files =  Label(self.Frame1, text = "Total Files: ", font = ("times new roman", 20), bg ="white")
        self.lbl_total_files.place(x = 10, y = 10)

        self.lbl_total_image = Label(self.Frame1, bd = 2, relief = RAISED, image = self.image_icon,compound=TOP, font = ("times new roman", 18, "bold"), bg = "#0066ff", fg = "white")
        self.lbl_total_image.place(x = 20, y = 60, width = 230, height = 200 )

        self.lbl_total_audio = Label(self.Frame1, bd = 2, relief = RAISED, image = self.audio_icon,compound=TOP, font = ("times new roman", 18, "bold"), bg = "#ffcc00", fg = "white")
        self.lbl_total_audio.place(x = 270, y = 60, width = 230, height = 200 )

        self.lbl_total_video = Label(self.Frame1, bd = 2, relief = RAISED, image = self.video_icon,compound=TOP, font = ("times new roman", 18, "bold"), bg = "#33cc33", fg = "white")
        self.lbl_total_video.place(x = 520, y = 60, width = 230, height = 200 )

        self.lbl_total_document = Label(self.Frame1, bd = 2, relief = RAISED, image = self.document_icon,compound=TOP, font = ("times new roman", 18, "bold"), bg = "#d11aff", fg = "white")
        self.lbl_total_document.place(x = 770, y = 60, width = 230, height = 200 )

        self.lbl_total_other = Label(self.Frame1, bd = 2, relief = RAISED, image = self.other_icon,compound=TOP, font = ("times new roman", 18, "bold"), bg = "grey", fg = "white")
        self.lbl_total_other.place(x = 1020, y = 60, width = 230, height = 200 )
        
        
        #======================================================= Section 4 =============================================================================================================================================================================================

        lbl_status = Label(self.root, text = "STATUS", font = ("times new roman", 20), bg ="white").place(x = 50, y = 630)
        self.lbl_st_total = Label(self.root, text = "", font = ("times new roman", 18), bg ="white", fg = "green")
        self.lbl_st_total.place(x = 300, y = 630)

        self.lbl_st_moved = Label(self.root, text = "", font = ("times new roman", 18), bg ="white", fg = "blue")
        self.lbl_st_moved.place(x = 500, y = 630)

        self.lbl_st_left = Label(self.root, text = "", font = ("times new roman", 18), bg ="white", fg = "orange")
        self.lbl_st_left.place(x = 700, y = 630)



        #======================================================= Buttons ================================================================================================================================================================================================
        self.btn_clear = Button(self.root, command = self.clear, text = "CLEAR", font = ("times new roman", 15, "bold"), bg = "#607d8b", fg = "white", activebackground = "#607d8b", cursor = "hand2", activeforeground = "white")
        self.btn_clear.place(x = 900, y = 630, height =  45, width = 200)
        self.btn_start = Button(self.root, state = DISABLED, command = self.start_function, text = "START", font = ("times new roman", 15, "bold"), bg = "#ff5722", fg = "white", activebackground = "#ff5722", cursor = "hand2", activeforeground = "white")
        self.btn_start.place(x = 1130, y = 630, height =  45, width = 200)

        button_1 = Button(self.root, text="Add Ext", font=("Calibri", 15, "bold"), command=self.show_frame_2, bg = "#FC12BE")
        button_1.place(x = 1380, y = 130, height =  45, width = 140)

        button_2 = Button(self.root, text="MAIN PAGE", font=("Calibri", 15, "bold"), command=self.show_frame_1, bg = "#FCF912")
        button_2.place(x = 1380, y = 200, height =  45, width = 140)

        button_3 = Button(self.root, text="Delete Ext", font=("Calibri", 15, "bold"), command=self.show_frame_3, bg = "#8FF6FF")
        button_3.place(x = 1380, y = 270, height =  45, width = 140)

        quit_button = Button(self.root, text="Quit", font=("Calibri", 15, "bold"), bg ="red", command=self.quit)
        quit_button.place(x = 1380, y = 340, height =  45, width = 140)
        
        
        #====================================================== Add Extension Frame (FRAME2) ================================================================================================================================================================================
        self.Frame2 = Frame(self.root, bd = 2, relief = RIDGE, bg = "#FF63F5")
        # self.Frame2.place(x= 50, y = 300, width = 1300, height = 300)
        self.var_radio = IntVar()

        #================================================== radio buttons for adding extension =====================================================================================================================================================================

        self.radio_Fr2_Image= Radiobutton(self.Frame2, text="Image Extension", variable=self.var_radio, value=1, bg = "#FF63F5", font=("Calibri", 15, "bold"),activebackground='#FF63F5',cursor='hand2')
        self.radio_Fr2_Image.place(x = 30, y = 60, width = 230, height = 200 )

        self.radio_Fr2_Audio= Radiobutton(self.Frame2, text="Audio Extensions", variable=self.var_radio, value=2, bg = "#FF63F5", font=("Calibri", 15, "bold"),activebackground='#FF63F5',cursor='hand2')
        self.radio_Fr2_Audio.place(x = 260, y = 60, width = 230, height = 200 )

        self.radio_Fr2_Video= Radiobutton(self.Frame2, text="Video Extension", variable=self.var_radio, value=3,bg = "#FF63F5", font=("Calibri", 15, "bold"),activebackground='#FF63F5',cursor='hand2')
        self.radio_Fr2_Video.place(x = 490, y = 60, width = 230, height = 200 )

        self.radio_Fr2_Document= Radiobutton(self.Frame2, text="Document Extension", variable=self.var_radio, value=4, bg = "#FF63F5", font=("Calibri", 15, "bold"),activebackground='#FF63F5',cursor='hand2')
        self.radio_Fr2_Document.place(x = 710, y = 60, width = 230, height = 200 )

        
        #======================================== Buttons for Adding Extensions  ======================================================================================================================================================================================================================

        self.var_F2_addext = StringVar()
        self.entry1_Fr2 = Entry(self.Frame2, textvariable = self.var_F2_addext, font = ("times new roman", 15), bg = "lightyellow").place(x = 90, y = 90, height = 40, width = 800)

        self.btn_Fr2_add = Button(self.Frame2, text = "Add", command=self.add_ext, font = ("times new roman", 15, "bold"), bg = "#262626", fg = "white", activebackground = "#262626", cursor = "hand2", activeforeground = "white").place(x = 900, y = 90, height =  45, width = 150)

        #=============================================================================================================================================================================================================================================================================================


        #======================================== Frame 3 =============================================================================================================================================================================================================================================
        self.Frame3 = Frame(self.root, bd = 2, relief = RIDGE, bg = "#8FF6FF")
        self.var_radio_Fr3 = IntVar()
        self.radio_Fr3_Image= Radiobutton(self.Frame3, text="Image Extension", variable=self.var_radio_Fr3, value=1, font=("Calibri", 15, "bold"), bg = "#8FF6FF", activebackground = "#8FF6FF", cursor="hand2", command=self.display_list)
        self.radio_Fr3_Image.place(x = 20, y = 70, width = 230, height = 50 )

        self.radio_Fr3_Audio= Radiobutton(self.Frame3, text="Audio Extension", variable=self.var_radio_Fr3, value=2, font=("Calibri", 15, "bold"), bg = "#8FF6FF", activebackground = "#8FF6FF", cursor="hand2",command=self.display_list)
        self.radio_Fr3_Audio.place(x = 270, y = 70, width = 230, height = 50 )

        self.radio_Fr3_Video= Radiobutton(self.Frame3, text="Video Extension", variable=self.var_radio_Fr3, value=3, font=("Calibri", 15, "bold"), bg = "#8FF6FF", activebackground = "#8FF6FF", cursor="hand2", command=self.display_list)
        self.radio_Fr3_Video.place(x = 20, y = 130, width = 230, height = 100 )

        self.radio_Fr3_Document= Radiobutton(self.Frame3, text="Document Extension", variable=self.var_radio_Fr3, value=4, font=("Calibri", 15, "bold"), bg = "#8FF6FF", activebackground = "#8FF6FF", cursor="hand2", command=self.display_list)
        self.radio_Fr3_Document.place(x = 270, y = 130, width = 230, height = 100 )

        self.lst_box = Listbox(self.Frame3, width=100, height=12,bg="lightgreen")
        self.lst_box.place(x=620,y=70)


        self.Fr3_btn_del = Button(self.Frame3, text="Delete",command=self.del_ele, font = ("times new roman", 15, "bold"), bg = "#262626", fg = "white", activebackground = "#262626", cursor = "hand2", activeforeground = "white")
        self.Fr3_btn_del.place(x = 160, y = 220, height =  45, width = 150)
    
    # Function to display the selected extension's content in list box
    def display_list(self):
        a=self.var_radio_Fr3.get()
        self.lst_box.delete(0, END)
        if a == 1:
            for item in self.image_extensions:
                self.lst_box.insert(END, item)
        elif a == 2:
            for item in self.audio_extensions:
                self.lst_box.insert(END, item)
        elif a == 3:
            for item in self.video_extensions:
                self.lst_box.insert(END, item)
        elif a == 4:
            for item in self.doc_extensions:
                self.lst_box.insert(END, item)
    

    # Function to retrieve the user selected element from list box to be deleted and update it in corresponding extension list and text file(JSON format)
    def del_ele(self):
        if not self.lst_box.curselection():
            messagebox.showerror("Error","Please select an extension to be deleted from Listbox !!!")
        self.deleted_element = self.lst_box.get(self.lst_box.curselection())
        self.lst_box.delete(ANCHOR) 
        a=self.var_radio_Fr3.get()
        self.lst_box_list=list(self.lst_box.get(0,END))
        # print(self.lst_box_list)
        if a == 1:
            self.path=path_imagefile
            self.image_extensions = self.lst_box_list
            self.update_extfile(self.path,self.image_extensions)
            self.image_box.config(values = self.image_extensions)
            messagebox.showinfo("Success",self.deleted_element+"Deleted from image extension")
        elif a == 2:
            self.path=path_audiofile
            self.audio_extensions = self.lst_box_list
            self.update_extfile(self.path,self.audio_extensions)
            self.audio_box.config(values = self.audio_extensions)
            messagebox.showinfo("Success",self.deleted_element+"Deleted from audio extension")
        elif a == 3:
            self.path=path_videofile
            self.video_extensions = self.lst_box_list
            self.update_extfile(self.path,self.video_extensions)
            self.video_box.config(values = self.video_extensions)
            messagebox.showinfo("Success",self.deleted_element+"Deleted from video extension")
        elif a == 4:
            self.path=path_docfile
            self.doc_extensions = self.lst_box_list
            self.update_extfile(self.path,self.doc_extensions)
            self.doc_box.config(values = self.doc_extensions)
            messagebox.showinfo("Success",self.deleted_element+"Deleted from document extension")



        
        #===============================================================================================================================================================  
    

    #=================================================== Button Functions to switch frames =============================================================================
    # Function to Open Frame 2
    def show_frame_2(self):
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.clear()
        self.btn_clear.config(state = DISABLED)
        self.Frame2.place(x= 50, y = 300, width = 1300, height = 300)
        
    #==================================================== Function to Open Frame 1 ======================================================================================
    def show_frame_1(self):
        self.btn_clear.config(state = ACTIVE)
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.Frame1.place(x= 50, y = 300, width = 1300, height = 300)

    #==================================================== Function to Open Frame 1 ======================================================================================
    def show_frame_3(self):
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.clear()
        self.btn_clear.config(state = DISABLED)
        self.Frame3.place(x= 50, y = 300, width = 1300, height = 300)
    #==================================================== Function to the update extension file after after/deleting =================================================================
    def update_extfile(self,path,extensions):
            try:
                with open(path, 'w') as f:
                    json.dump(extensions, f)
                    
                
                # with open(path, 'r') as f:
                #     print("after updating",f.read())
            
            except Exception as e:
                print(e)
    #======================================================================================================================================================================
    
    #================================== Function to Append/Add an extension to list =======================================================================================
    
    def add_ext(self):
        a=self.var_radio.get()
        b="."+self.var_F2_addext.get()
  
        if a == 0:
            messagebox.showerror("Error","Please select an extension !!!") 
        else:
            if b == "." or "":
                messagebox.showerror("Error","Extension cannot be empty or '.' !!!")
            else:
                if a == 1:
                    self.path=path_imagefile        
                    if self.image_extensions is not None and b  in self.image_extensions:
                        messagebox.showerror("Error: ",b+" the extension already exits !!!")
                    elif self.image_extensions is None:
                        messagebox.showerror("Error:", "image_extension is EMPTY")
                        # print(self.image_extensions)
                    else:
                        self.image_extensions.append(b)
                        self.update_extfile(self.path,self.image_extensions)
                        self.image_box.config(values = self.image_extensions)
                        # print(self.folders)
                        messagebox.showinfo("Success",b+" Extension added to image")       
                elif a == 2:
                    self.path=path_audiofile
                    if self.audio_extensions is not None and b in self.audio_extensions:
                        messagebox.showerror("Error: ",b+" the extension already exits !!!")
                    elif self.audio_extensions is None:
                        messagebox.showerror("Error:", "audio_extension is EMPTY")
                        # print(self.audio_extensions)
                    else:
                        self.audio_extensions.append(b)
                        self.update_extfile(self.path,self.audio_extensions)
                        self.audio_box.config(values = self.audio_extensions)
                        # print(self.folders)
                        messagebox.showinfo("Success",b+" Extension added to audio")

                elif a == 3:
                    self.path=path_videofile
                    if self.video_extensions is not None and b in self.video_extensions:
                        messagebox.showerror("Error: ",b+" the extension already exits !!!")
                    elif self.video_extensions is None:
                        messagebox.showerror("Error:", "video_extension is EMPTY")
                        print(self.video_extensions)
                    else:
                        self.video_extensions.append(b)
                        self.update_extfile(self.path,self.video_extensions)
                        self.video_box.config(values = self.video_extensions)
                        # print("Thank you succesfully")
                        messagebox.showinfo("Success",b+" Extension added to video")

                elif a == 4:
                    self.path=path_docfile
                    if self.doc_extensions is not None and b in self.doc_extensions:
                        messagebox.showerror("Error: ",b+" the extension already exits !!!")
                    elif self.doc_extensions is None:
                        messagebox.showerror("Error:", "doc_extension is EMPTY")
                        print(self.doc_extensions)
                    else:
                        self.doc_extensions.append(b)
                        self.update_extfile(self.path,self.doc_extensions)
                        self.doc_box.config(values = self.doc_extensions)
                        # print("Thank you succesfully")
                        messagebox.showinfo("Success",b+" Extension added to documents")


    #=================================================================================================================================================================
    
    #======================================================= Function to keep track of files count ===================================================================
    #it keeps track of the files count after browsing a path  
    
    def Total_count(self):
        images = 0
        audios = 0
        videos = 0
        documents = 0
        others = 0
        self.count = 0
        combine_list = []
    
        for self.root_path,self.sub_dir,self.files in os.walk(self.directry):
            self.all_files = os.listdir(self.root_path)
            length = len(self.all_files)
            count = 1
            folder_name = os.path.basename(self.root_path)
            for i in self.all_files:
                if folder_name not in self.folders_list:
                    if os.path.isfile(os.path.join(self.root_path,i)) == True:
                        self.count += 1
                        ext = "."+i.split(".")[-1]
                        for folder_name in self.folders.items():
                            #print(folder_name)
                            for x in folder_name[1]:
                                combine_list.append(x)
                            if ext.lower() in folder_name[1] and folder_name[0] == "images":
                                images += 1 
                            if ext.lower() in folder_name[1] and folder_name[0] == "audios":
                                audios += 1
                            if ext.lower() in folder_name[1] and folder_name[0] == "videos":
                                videos += 1
                            if ext.lower() in folder_name[1] and folder_name[0] == "documents":
                                documents += 1
            # This is for Calculating Other Files ONLY  
            for self.root_path,self.sub_dir,self.files in os.walk(self.directry):
                self.all_files = os.listdir(self.root_path)
                folder_name = os.path.basename(self.root_path)
                for i in self.all_files:
                    if folder_name not in self.folders_list:
                        if os.path.isfile(os.path.join(self.root_path,i)) == True:
                            ext = "."+i.split(".")[-1]
                            if ext.lower() not in combine_list:
                                others += 1
                        

        self.lbl_total_image.config(text = "Total Images \n"+str(images))
        self.lbl_total_video.config(text = "Total Videos \n"+str(videos))
        self.lbl_total_audio.config(text = "Total Audios \n"+str(audios))
        self.lbl_total_document.config(text = "Total Documents \n"+str(documents))
        self.lbl_total_other.config(text = "Other files or folders \n"+str(others))
        self.lbl_total_files.config(text = "Total Files: "+str(self.count))

 

    #================================================ Function to browse a path for sorting =========================================================================================
    def browse_function(self):
        op = filedialog.askdirectory(title = "SELECT FOLDER FOR SORTING")
        if op != None:
            self.var_foldername.set(str(op))
            self.directry =  self.var_foldername.get()
            self.other_name = "others"
            self.rename_folder()
            self.Total_count()
            self.btn_start.config(state = NORMAL)

    def start_function(self):
        if self.var_foldername.get() != "":
            self.btn_clear.config(state = DISABLED)
            c = 0
            for self.root_path,self.sub_dir,self.files in os.walk(self.directry):
                for i in self.files:
                    folder_name = os.path.basename(self.root_path)
                    # print(folder_name)
                    if folder_name not in self.folders_list:
                        if os.path.isfile(os.path.join(self.root_path,i)) == True:
                            #print("yes")
                            c += 1
                            self.create_move(i.split(".")[-1],i)
                            self.lbl_st_total.config(text = "TOTAL: "+str(self.count))
                            self.lbl_st_moved.config(text = "MOVED: "+str(c))
                            self.lbl_st_left.config(text = "LEFT: "+str(self.count-c))

                            self.lbl_st_total.update()
                            self.lbl_st_moved.update()
                            self.lbl_st_left.update()

            messagebox.showinfo("Success","All files has been moved sucessfully")
            self.btn_start.config(state = DISABLED)
            self.btn_clear.config(state = NORMAL)
        else:
            messagebox.showerror("Error","Please select folder")

    #================================================== Function to quit the screen ===========================================================================================
    def quit(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


    #================================================== Function to clear the contents of previous sorted folders =============================================================
    def clear(self):
        self.btn_start.config(state = DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text = "")
        self.lbl_st_moved.config(text = "")
        self.lbl_st_left.config(text = "")

        self.lbl_total_image.config(text = "")
        self.lbl_total_video.config(text = "")
        self.lbl_total_audio.config(text = "")
        self.lbl_total_document.config(text = "")
        self.lbl_total_other.config(text = "")
        self.lbl_total_files.config(text = "Total Files: ")

    #======================================================== Rename Function ======================================================================================
    #converts the file names to lower case to ease the sorting

    def rename_folder(self):
        for self.root_path,self.sub_dir,self.filenames in os.walk(self.directry):
            for folder in os.listdir(self.root_path):
                if os.path.isdir(os.path.join(self.root_path,folder)) == True:
                    os.rename(os.path.join(self.root_path,folder),os.path.join(self.root_path,folder.lower()))


    #======================================================= Move Function =========================================================================================
    def create_move(self,ext,file_name):
        find = False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.root_path):
                        os.mkdir(os.path.join(self.root_path,folder_name))
                shutil.move(os.path.join(self.root_path,file_name),os.path.join(self.root_path,folder_name))
                find = True
                break

        if find != True:
            if self.other_name not in os.listdir(self.root_path):
                os.mkdir(os.path.join(self.root_path,self.other_name))
            shutil.move(os.path.join(self.root_path,file_name),os.path.join(self.root_path,self.other_name))

root = Tk()
obj = Sorting_App(root)
root.mainloop()
