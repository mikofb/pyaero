"""
    Author:
            → Name: Brou Koffi Franck Michael
            → Country: Ivory Coast
            → City: Abidjan
            → Phone : (+225) 44908473/89367484
            → Email: broukoffifranckmichael@gmailcom
            → Linkedin: https://www.linkedin.com/in/brou-koffi-franck-michael-969334167
            → School: Ecole Superieure Africaine des TIC (ESATIC)

    Comments:        
        PyAero is a mini file explorer designed and coded with the python librairy Tkinter
        It allows some actions such as:
            → browse a directory
            → delete a file or directory
            → rename a file or directory
            → create a file or directory
            → search a file or directory
            → launch/play/display any file if its corresponding app is allready installed
            → Etc...
             
    Notice:
            → Version: 1.0 bêta
            → Platform: windows
            → Python version: 3.4

                    ♥ Feel free to send any comments, suggestions about this app

    Credentials:
            → Google
            → Stackoverflow
            → Youtube
            → Github
"""
import os
import threading
from tkinter import *
import tkinter.messagebox 
import FileModule
import PopupWindows
from Settings import loader

#------------------------------
#---[ PyAero GLOBAL PARAMS ]---
#------------------------------

PARAMS = ['Mini File Manager - PyAero 1.0','flat']

FONTS = ['Helvetica 10',"Helvetica 9",'Helvetica 11']

COLORS = ["#6c6d69","#ebebeb","#10a4dc","#6c6d69","#5599ff","#b5b5b5","#fcfcfc"]

IMAGES_DIRECTORY = os.getcwd()+'\\img'

HOME_PATH = os.path.expanduser('~') 

IMAGES = loader.IMAGES
MAIN_WORDS = loader.MAIN_WORDS
CONTEXT_MENU = loader.CONTEXT_MENU
LEFT_SIDE_WORDS = loader.LEFT_SIDE_WORDS
OTHERS_WORDS = loader.OTHERS_WORDS
FILE_NAME = loader.FILE_NAME

COMMON_POPUP_WORDS = loader.COMMON_POPUP_WORDS
RENAME_POPUP = loader.RENAME_POPUP
DELETE_POPUP = loader.DELETE_POPUP
NEW_POPUP = loader.NEW_POPUP
PROPERTIES_POPUP = loader.PROPERTIES_POPUP
SETTINGS_POPUP = loader.SETTINGS_POPUP
ABOUT_POPUP = loader.ABOUT_POPUP

MAIN_PATHS = ['Desktop','Documents','Pictures','Music','Videos','Downloads']

PATHS = []
drives = []
drives_buttons = []
search_path = []

disk_name = ''


"""
    MAIN CLASS PyAero
"""
class PyAero():

    def __init__(self):

    #----------------------------
    #---[ PyAero GUI SETTING ]---
    #----------------------------
        self.window = Tk()
        self.window.withdraw()
        self.window.resizable(False, False)
        self.window.config(bg=COLORS[1])
        self.window.wm_title(PARAMS[0])
        self.window.iconbitmap(bitmap=os.path.join(IMAGES_DIRECTORY,IMAGES[0]))
        self.src = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[1]))
        self.splash = Toplevel()
        self.search_splash = None
        self.splash.overrideredirect(1)
        self.splash.geometry('500x400+450+200')
        self.splash.bind('<1w>Root')
        Label(self.splash, text='',image = self.src).pack()
        self.window.after(3000, self.showRoot)
    #----------------------------------------
    #---[ CREATING COMPONENTS ON THE GUI ]---
    #----------------------------------------
        self.main_frame = Frame(self.window, bg= COLORS[1])
        self.header_frame = Frame(self.main_frame, bg = COLORS[0])
        #--- The PyAero navbar 
        self.nav_frame = Frame(self.header_frame, bg=COLORS[1])
        self.prev_button = Button(self.nav_frame, relief=FLAT, bg=COLORS[6], command= self.prev)
        self.next_button = Button(self.nav_frame, relief=FLAT, bg=COLORS[6], command = self.next)
        self.refresh_button = Button(self.nav_frame, relief=FLAT, bg=COLORS[6], command=self.refresh)
        self.addressBar_entry = Entry(self.nav_frame, relief=FLAT, bg=COLORS[6], width=80, font=FONTS[1], bd = 2, selectbackground=COLORS[2], highlightthickness=1, highlightcolor=COLORS[2], insertwidth=1)
        self.researchBar_entry = Entry(self.nav_frame, relief=FLAT, bg=COLORS[6], width=25, font=FONTS[1], bd = 2, selectbackground=COLORS[2], highlightthickness=1, highlightcolor=COLORS[2], insertwidth=1)
        self.researchBar_button = Button(self.nav_frame, relief=FLAT, bg=COLORS[6], command = self.research_dispatcher)
        self.separator = Frame(self.main_frame, bg=COLORS[5], height=1)
        #--- The PyAero taskbar 
        self.taskBar_frame = Frame(self.window, bg='white')
        self.file_number = Label(self.taskBar_frame, font=FONTS[1])
        self.dirs_number = Label(self.taskBar_frame, text = '', font=FONTS[1])
        self.files_number = Label(self.taskBar_frame, text = '', font=FONTS[1])
        #--- The PyAero explorewindow 
        self.explore_window = PanedWindow(self.main_frame, bg=COLORS[1], orient= 'horizontal',  border=0, height=550, relief=FLAT)
        #--- The PyAero leftside window
        self.arch_frame = PanedWindow(self.explore_window, orient= 'vertical', relief=FLAT, bg=COLORS[1], borderwidth=2)
        self.lib_frame = Frame(self.arch_frame, bg=COLORS[1])
        self.lib_frame.name = Label(self.lib_frame, text=LEFT_SIDE_WORDS[0], relief=PARAMS[1], bg=COLORS[1], anchor='nw')
        self.desktop_button = Button(self.lib_frame, border=0, text=' {}'.format(LEFT_SIDE_WORDS[1]), relief=PARAMS[1], anchor='nw', command=self.explore_desktop, bg='white')
        self.documents_button = Button(self.lib_frame, border=0, text=' {}'.format(LEFT_SIDE_WORDS[2]), relief=PARAMS[1], anchor='nw', command=self.explore_document, bg='white')
        self.images_button = Button(self.lib_frame, border=0, text=' {}'.format(LEFT_SIDE_WORDS[3]), relief=PARAMS[1], anchor='nw', command=self.explore_image, bg='white')
        self.music_button = Button(self.lib_frame, border=0, text=' {}'.format(LEFT_SIDE_WORDS[4]), relief=PARAMS[1], anchor='nw', command=self.explore_music, bg='white')
        self.videos_button = Button(self.lib_frame, border=0, text=' {}'.format(LEFT_SIDE_WORDS[5]), relief=PARAMS[1], anchor='nw', command=self.explore_video, bg='white')
        self.downloads_button = Button(self.lib_frame, border=0, text=' {}'.format(LEFT_SIDE_WORDS[6]), relief=PARAMS[1], anchor='nw', command=self.explore_download, bg='white')
        #--- The PyAero disk frame
        self.disk_frame = Frame(self.arch_frame, bg=COLORS[1])
        self.disk_frame.name = Label(self.disk_frame, text=LEFT_SIDE_WORDS[7], bg=COLORS[1], anchor='nw')
        #--- The PyAero configuration frame
        self.config_frame = Frame(self.arch_frame, border=0, bg=COLORS[1])
        self.config_frame.name = Label(self.config_frame, text=LEFT_SIDE_WORDS[9], bg=COLORS[1], anchor='nw')
        self.config_settings_button = Button(self.config_frame, border=0, highlightbackground= COLORS[1], text=' {}'.format(LEFT_SIDE_WORDS[10]), anchor='nw', relief=PARAMS[1], command=self.show_settings, bg='white')
        self.config_about_button = Button(self.config_frame, border=0, highlightbackground= COLORS[1], text=' {}'.format(LEFT_SIDE_WORDS[11]), anchor='nw', relief=PARAMS[1], command=self.show_about, bg='white')
        #--- The PyAero rightside window
        self.result_frame = Frame(self.explore_window, bg='white')
        self.resultDisplay_frame = Listbox(self.result_frame, width = 60, relief=PARAMS[1], highlightbackground= 'white', bg= 'white', bd=0, selectbackground=COLORS[2], activestyle='none',font=FONTS[0])
        self.resultDisplay_frame_file_info = Frame(self.result_frame, height= 300, width=230, border=0, bg='white', relief=PARAMS[1], bd=0)
        #--- The PyAero desription
        self.description_icon_label = Label(self.resultDisplay_frame_file_info, bg='white')
        self.description_type_label = Label(self.resultDisplay_frame_file_info, bg='white', text='')
        self.description_date_label = Label(self.resultDisplay_frame_file_info, bg='white', text='')
        self.description_size_label = Label(self.resultDisplay_frame_file_info, bg='white', text='')
        self.scrollbary = Scrollbar(self.result_frame, border=0, orient='vertical')
        self.scrollbary.config(command=self.resultDisplay_frame.yview)
        self.resultDisplay_frame.config(yscrollcommand=self.scrollbary.set)
        #--- The PyAero contextmenu
        self.context_menu = Menu(self.resultDisplay_frame)
        self.context_menu.add_command(label=CONTEXT_MENU[0], command=self.open)
        self.context_menu.add_command(label=CONTEXT_MENU[1], command=self.zip_file)
        self.context_menu.add_command(label=CONTEXT_MENU[2], command=self.unzip_file)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=CONTEXT_MENU[3], command=self.copy_file)
        self.context_menu.add_command(label=CONTEXT_MENU[4], command=self.cut_file)
        self.context_menu.add_command(label=CONTEXT_MENU[5], command=self.paste_file)
        self.context_menu.add_command(label=CONTEXT_MENU[6], command=self.delete_file)
        self.context_menu.add_command(label=CONTEXT_MENU[7], command=self.rename_file)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=CONTEXT_MENU[8], command=self.new)
        self.context_menu.add_command(label=CONTEXT_MENU[9], command=self.show_prop)
        #--- The PyAero pictures
        self.prev = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[2]))
        self.prev_button.config(image= self.prev)
        self.next = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[3]))
        self.next_button.config(image=self.next)
        self.ref = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[4]))
        self.refresh_button.config(image=self.ref)
        self.desk = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[5]))
        self.desktop_button.config(image=self.desk, compound= LEFT)
        self.dcmt = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[6]))
        self.documents_button.config(image=self.dcmt, compound= LEFT)
        self.img = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[7]))
        self.images_button.config(image=self.img, compound= LEFT)
        self.mus = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[8]))
        self.music_button.config(image=self.mus, compound= LEFT)
        self.video = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[9]))
        self.videos_button.config(image=self.video, compound= LEFT)
        self.dl = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[10]))
        self.downloads_button.config(image=self.dl, compound= LEFT)
        self.disk = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[11]))
        self.net = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[12]))
        self.config_settings_button.config(image=self.net, compound= LEFT)
        self.netmach = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[13]))
        self.config_about_button.config(image=self.netmach, compound= LEFT)
        self.folder = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[14]))
        self.archive_folder = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[15]))
        self.music_file = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[16]))
        self.video_file = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[17]))
        self.pdf_file = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[18]))
        self.other_file = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[19]))
        self.picture = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[20]))
        self.link = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[21]))
        self.python = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[22]))
        self.php = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[23]))
        self.powerpoint = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[24]))
        self.html = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[25]))
        self.java = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[26]))
        self.exe = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[27]))
        self.excel = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[28]))
        self.css = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[29]))
        self.cpp = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[30]))
        self.c = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[31]))
        self.access = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[32]))
        self.word = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[33]))
        self.text = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[34]))
        self.crt = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[35]))
        self.disk_image = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[36]))
        self.dll = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[37]))
        self.header = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[38]))
        self.htm = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[39]))
        self.log = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[40]))
        self.perl = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[41]))
        self.rpm = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[42]))
        self.rtf = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[43]))
        self.sql = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[44]))
        self.xml = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[45]))
        self.deb = PhotoImage(file=os.path.join(IMAGES_DIRECTORY,IMAGES[46]))

    #---------------------------------------
    #---[ PACKING COMPONENTS ON THE GUI ]---
    #---------------------------------------

        self.main_frame.pack(fill = BOTH, expand = True)
        self.header_frame.pack(side=TOP, fill = X, pady=2)
        self.nav_frame.pack(side = TOP, fill = X)
        self.prev_button.pack(side=LEFT, padx=2,pady=2)
        self.next_button.pack(side=LEFT, padx=2,pady=2)
        self.addressBar_entry.pack(side=LEFT,pady=2)
        self.refresh_button.pack(side=LEFT, pady=2)
        self.researchBar_entry.pack(side=RIGHT,padx=1, pady=2)
        self.separator.pack(side=TOP, fill=X)
        self.explore_window.pack(fill = BOTH, expand = True)
        self.explore_window.add(self.arch_frame, minsize=170)
        self.explore_window.add(self.result_frame)
        
        self.lib_frame.pack(side = TOP,fill=BOTH)
        self.lib_frame.name.pack(side=TOP, fill=X)
        self.desktop_button.pack(side = TOP,fill=X)
        self.documents_button.pack(side = TOP,fill=X)
        self.images_button.pack(side = TOP,fill=X)
        self.music_button.pack(side = TOP,fill=X)
        self.videos_button.pack(side = TOP,fill=X)
        self.downloads_button.pack(side = TOP,fill=X)
        
        self.disk_frame.pack(side = TOP,fill=BOTH)
        self.disk_frame.name.pack(side=TOP, fill=X)
        
        self.config_frame.pack(fill=BOTH)
        self.config_frame.name.pack(side=TOP, fill=X)
        self.config_settings_button.pack(side = TOP,fill=X)
        self.config_about_button.pack(side = TOP,fill=X)

        self.resultDisplay_frame.pack(side = LEFT, fill=BOTH, padx=5, expand = True)
        self.resultDisplay_frame_file_info.pack(side = LEFT, fill=BOTH, expand = True)
        self.description_type_label.pack(side=BOTTOM, fill=X)
        self.description_date_label.pack(side=BOTTOM, fill=X)
        self.description_size_label.pack(side=BOTTOM, fill=X)
        self.description_icon_label.pack(side=BOTTOM, fill=Y)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        
        self.taskBar_frame.pack(side= BOTTOM, fill=Y)
        self.file_number.pack(side=LEFT)
        self.dirs_number.pack(side=LEFT)
        self.files_number.pack(side=LEFT)

        self.explore_window.pack(fill=BOTH)

    #---------------------------------------------
    #---[ BINDING EVENTS TO SPECIFICS METHODS ]---
    #---------------------------------------------

        self.resultDisplay_frame.bind("<<ListboxSelect>>", self.load_file_info)
        self.resultDisplay_frame.bind('<Double-1>', self.double)
        self.resultDisplay_frame.bind('<Button-3>', self.popup)
        self.resultDisplay_frame.bind('<Return>',self.double)
        self.resultDisplay_frame.bind('<Delete>',lambda x: self.delete_file())
        self.addressBar_entry.bind('<Return>', lambda x: self.explore(self.addressBar_entry.get()))
        self.addressBar_entry.bind("<FocusIn>", lambda x: self.addressBar_entry.select_range(0,END))
        self.researchBar_entry.bind('<Return>', lambda x: self.research_dispatcher())
        self.researchBar_entry.bind("<FocusIn>", self.focus_in)
        self.researchBar_entry.bind("<FocusOut>", self.focus_out)

    #--------------------------------------------------
    #---[ THE DIFFERENTS METHODS USED IN PyAero UI ]---
    #--------------------------------------------------

        """
            DISPATCHING METHODS:
            --------------------
        """
    def research_dispatcher(self):
        " Calls specific thread for the given regrex expression"
        search_temp = self.researchBar_entry.get()
        path = self.addressBar_entry.get()
        self.init_display()
        if search_temp == '':
            tkinter.messagebox.showwarning(MAIN_WORDS[0],MAIN_WORDS[1])
        else:
            if search_temp.startswith("/"):
                self.search_file_thread(self.add,path,'')
            else:
                self.search_file_thread(self.add_file,path,search_temp)

    def explore_disk_dispatcher(self, f):
        "Explores the device by their name @f"
        global disk_name
        disk_name = f
        self.explore(f[len(f)-3]+':\\')

        """
            THREADS METHODS:
            ----------------
        """
    def search_file_thread(self,func,path,temp):
        if self.addressBar_entry.get() !='':
            threading.Thread(target=func, args=(path,temp)).start()

        """
            MAIN METHODS:
            ------------
        """

    def main(self):
        "Main method called just after initializing the @PyAero instanciation"
        self.explore(HOME_PATH)
        self.list_disk()
        self.window.mainloop()

    def showRoot(self, *args):
        self.splash.destroy()
        self.window.deiconify()
        self.center(self.window)

    def center(self,win):
        "Center the main window to the screen"
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def init_display(self):
        """
            Initializes every display frame or widget such as:
                the Listbox that displays results
                the task bar Labels
                the files descriptors (for the pictures, the type, the size)
        """
        self.resultDisplay_frame.delete(0, END)
        self.description_icon_label.config(image='')
        self.description_type_label.config(text='')
        self.description_size_label.config(text='')
        self.description_date_label.config(text='')
        self.file_number.config(text='')
        self.dirs_number.config(text='')
        self.files_number.config(text='')

    def load_path(self):
        """
            Explores the current path in the address bar
        """
        p = self.addressBar_entry.get()
        if p !='':
            self.explore(p)

    """
        RESEARCH METHODS:
        ----------------
    """
    def add(self,path,ext):
        """
            Searchs every file in @path which ends with blank extention @ext and displays them in @resultDisplay_frame
        """
        
        #------------------------------------
        #   Screen splash     
        #------------------------------------
        self.show_splash()
        #------------------------------------
        
        res = FileModule.findFileByExtension(path, ext)[0]
        self.file_number['text'] = '{0} {1}'.format(len(res), MAIN_WORDS[4])
        if res == []:
            tkinter.messagebox.showwarning(MAIN_WORDS[5], MAIN_WORDS[6])
        else:
            for f in res:
                try:
                    self.resultDisplay_frame.insert(END,'{}'.format(f))
                except TclError:
                    pass
        search_path = FileModule.findFileByExtension(path, ext)[1]
        self.destroy_splash()

    def add_file(self,path,template):
        """
            Searchs dirname and filename recursively in @path which contains the @template and displays them in @resultDisplay_frame
        """
        dirn_number = 0
        file_number = 0
        
        #------------------------------------
        #   Screen splash     
        #------------------------------------
        self.show_splash()
        #------------------------------------

        global search_path
        for dirpaths, dirnames, filenames in os.walk(path):
            for dirn in dirnames:
                if template.lower() in dirn.lower():
                    dirn_number = dirn_number+1
                    self.resultDisplay_frame.insert(END,'{}'.format(dirn))
            for file in filenames:
                if template.lower() in file.lower():
                    file_number = file_number+1
                    try:
                        self.resultDisplay_frame.insert(END,'{}'.format(file))
                    except TclError:
                        pass
                    search_path.append(os.path.join(dirpaths,file))
                    self.file_number['text'] = '{0} {1} |'.format(dirn_number+file_number, MAIN_WORDS[2])
                    self.dirs_number['text'] = '{0} {1} |'.format(dirn_number, MAIN_WORDS[3])
                    self.files_number['text'] = '{0} {1}'.format(file_number, MAIN_WORDS[4])
        self.destroy_splash()
        if dirn_number == 0 and file_number == 0:
            tkinter.messagebox.showwarning(MAIN_WORDS[5], MAIN_WORDS[6])
    

    """
        NAVIGATION METHODS:
        -------------------
    """
    def prev(self):
        """
            Explores previous directories by clicking the prev_button
        """
        if len(PATHS) != 0:
            if self.addressBar_entry.get() == PATHS[0]:
                return
            else:
                for x in range(len(PATHS)):
                    if PATHS[x] == self.addressBar_entry.get():
                        self.explore(PATHS[x-1])
                        return

    def next(self):
        """
            Explores next directories by clicking the next_button
        """
        if len(PATHS) !=0:
            for x in range(len(PATHS)):
                if PATHS[x] == self.addressBar_entry.get():
                    try:
                        self.explore(PATHS[x+1])
                    except IndexError:
                        pass
                    return

    def refresh(self):
        """
            Refreshs @resultDisplay_frame by exploring the path in @addressBar_entry
        """
        if self.addressBar_entry.get() != '':
            self.explore(self.addressBar_entry.get())
        else:
            self.prev()                      

    
    """
        METHODS FOR EXPLORATION:
        -----------------------
    """
    def explore_desktop(self):
        """
            Lists every folder and files on the desktop
        """
        self.explore(os.path.join(HOME_PATH,MAIN_PATHS[0]))

    def explore_document(self):
        """
            Lists every folder and files in the document folder
        """
        self.explore(os.path.join(HOME_PATH,MAIN_PATHS[1]))

    def explore_image(self):
        """
            Lists every folder and files in the pictures folder
        """
        self.explore(os.path.join(HOME_PATH,MAIN_PATHS[2]))

    def explore_music(self):
        """
            Lists every folder and files in the documents folder
        """
        self.explore(os.path.join(HOME_PATH,MAIN_PATHS[3]))

    def explore_video(self):
        """
            Lists every folder and files in the video folder
        """
        self.explore(os.path.join(HOME_PATH, MAIN_PATHS[4]))

    def explore_download(self):
        """
            Lists every folder and files in the download folder
        """
        self.explore(os.path.join(HOME_PATH, MAIN_PATHS[5]))

    def explore(self, path):
        """
            Lists directories and files in the given path
        """
        self.init_display()
        for dirpaths, dirnames, filnames in os.walk(path):
            if self.addressBar_entry.get() !='':
                self.addressBar_entry.delete(0, END)
            self.addressBar_entry.insert(len(self.addressBar_entry.get()), path)
            if not path in PATHS:
                PATHS.append(path)
            for dirname in dirnames:
                self.resultDisplay_frame.insert(END,'{}'.format(dirname))
            for file in filnames:
                try:
                    self.resultDisplay_frame.insert(END,'{}'.format(file))
                except TclError:
                    pass
                self.file_number['text'] = '{0} {1}  |'.format(len(dirnames)+len(filnames), MAIN_WORDS[2])
                self.dirs_number['text'] = '{0} {1}  |'.format(len(dirnames), MAIN_WORDS[3])
                self.files_number['text'] = '{0} {1}'.format(len(filnames), MAIN_WORDS[4])
            self.focus_out()
            return        

    """
        SETTINGS AND ABOUT METHODES
        ---------------------------
    """
    def show_settings(self):
        """
            Shows the settings window
        """
        setting = PopupWindows.Settings(SETTINGS_POPUP[0])
        self.set_prior(setting)

    def show_about(self):
        """
            Shows the about window
        """
        about = PopupWindows.About(ABOUT_POPUP[0])
        self.set_prior(about)

    """
        CONTEXT MENU METHODS:
        --------------------
    """
    def open(self):
        """
            Context menu open command
        """
        self.double()
    
    def zip_file(self):
        ""

    def unzip_file():
        ""

    def copy_file(self):
        ""

    def cut_file():
        ""

    def paste_file(self):
        ""

    def delete_file(self):
        """
            Deletes current select item in @resultDisplay_frame
        """
        select = os.path.join(self.addressBar_entry.get(),self.resultDisplay_frame.get(self.resultDisplay_frame.curselection()))
        try:
            try:
                try:
                    req = PopupWindows.Delete(select, DELETE_POPUP, COMMON_POPUP_WORDS)
                    self.set_prior(req)
                except TclError:
                    pass
            except TypeError:
                pass
        except FileNotFoundError:
            pass
        finally:
            self.explore(self.addressBar_entry.get())

    def rename_file(self):
        "Rename the current folder or the current file by calling the rename dialogbox"
        try:
            try:
                try:
                    ren = PopupWindows.Rename(os.path.join(self.addressBar_entry.get(),self.resultDisplay_frame.get(self.resultDisplay_frame.curselection())), RENAME_POPUP, COMMON_POPUP_WORDS)
                    self.set_prior(ren)
                except TclError:
                    pass
            except TypeError:
                pass
        except FileNotFoundError:
            pass
        finally:
            self.explore(self.addressBar_entry.get())    

    def new(self):
        """
            Creates a new folder or a new file in the current directory
        """
        new = PopupWindows.New(self.addressBar_entry.get(), NEW_POPUP, COMMON_POPUP_WORDS)
        self.set_prior(new)
        self.explore(self.addressBar_entry.get())

    def show_prop(self):
        """
           Shows the properties of the selected item in the listbox 
        """
        prop = PopupWindows.Properties(PROPERTIES_POPUP,os.path.join(self.addressBar_entry.get(),self.resultDisplay_frame.get(self.resultDisplay_frame.curselection())))
        self.set_prior(prop)

    def popup(self,event):
        """
            Displays the context menu
        """
        if self.resultDisplay_frame.curselection() != None:
            self.context_menu.post(event.x_root, event.y_root)

    def double(self, *args):
        """
            Explores the current selected item from the resultDisplay_frame Listbox if it's a folder
        """
        try:
            select = os.path.join(self.addressBar_entry.get(),self.resultDisplay_frame.get(self.resultDisplay_frame.curselection()))
            if os.path.isdir(select):
                self.explore(select)
            else:
                try:
                    os.startfile(select)
                except FileNotFoundError:
                    for p in search_path:
                        if self.resultDisplay_frame.get(self.resultDisplay_frame.curselection()) in p:
                            os.startfile(p)
                            break
        except TclError:
            pass
    
    """
        COMPLEMENTARY METHODS:
        ---------------------
    """
    def list_disk(self):
        """
            Lists every connected devices on the computer
        """
        L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        name = ""
        for d in L:
            if os.path.isdir(d + ':/'):
                drives.append(d)
        for i in drives:
            if FileModule.get_device_name(i)=="":
                name = LEFT_SIDE_WORDS[8]
            else:
                name = FileModule.get_device_name(i)
            button_text = '{0} ({1}:)'.format(name,i)
            di = Button(self.disk_frame, text=' {}'.format(button_text), border=0, highlightbackground= COLORS[1], anchor='nw', command=lambda j=button_text: self.explore_disk_dispatcher(j),relief=PARAMS[1], bg='white')
            di.pack(side = TOP,fill=X)
            di.config(image=self.disk, compound= LEFT)
            drives_buttons.append(di)

    def show_splash(self):
        """
            Shows the screen splash when looking for file 
        """
        self.search_splash = Toplevel(bg='#235864')
        self.search_splash.overrideredirect(1)
        self.search_splash.geometry('300x100+450+300')
        self.search_splash.bind('<1w>Root')
        Label(self.search_splash, bg='#235864', fg='white', text=OTHERS_WORDS[2], font="Times 20 normal").pack(side=TOP, padx=30, pady=30)

    def destroy_splash(self):
        """
            Destroys the search screen splash when the research is over
        """
        self.search_splash.destroy()

    def set_prior(self, obj):
        """
            Sets the priority to a Toplevel window
        """
        obj.transient(self.window)
        obj.grab_set()
        self.window.wait_window(obj)

    def focus_in(self, *args):
        """
            Focus in the research bar
        """
        self.researchBar_entry.config(fg='black')
        self.researchBar_entry.delete(0, END)
            
    def focus_out(self, *args):
        """
            Focus out the research bar
        """
        self.researchBar_entry.delete(0, END)
        self.researchBar_entry.config(fg='grey')
        dirn = FileModule.get_dirname(self.addressBar_entry.get(), disk_name)
        if dirn == 'Desktop':
            dirn = LEFT_SIDE_WORDS[1]
        elif dirn == 'Pictures':
            dirn = LEFT_SIDE_WORDS[3]
        elif dirn == 'Music':
            dirn = LEFT_SIDE_WORDS[4]
        elif dirn == 'Videos':
            dirn = LEFT_SIDE_WORDS[5]
        elif dirn == 'Downloads':
            dirn = LEFT_SIDE_WORDS[6]
        else:
            pass
        researchBar_text = '{0}: {1}'.format(OTHERS_WORDS[0],dirn)
        if len(researchBar_text)>self.researchBar_entry['width']:
            researchBar_text = researchBar_text[:self.researchBar_entry['width']+1]+'...'
        self.researchBar_entry.insert(0, '{}'.format(researchBar_text))
    
    def load_file_info(self, prest):
        """
            Load file in
        """
        try:
            elmt = os.path.join(self.addressBar_entry.get(), self.resultDisplay_frame.get((self.resultDisplay_frame.curselection())))
            selectItem = self.resultDisplay_frame.get((self.resultDisplay_frame.curselection()))
            ext = FileModule.get_file_extension(selectItem).lower()
            if os.path.isdir(elmt):
                self.description_icon_label.config(image=self.folder)
                self.description_type_label.config(text=FILE_NAME[32])
                self.description_size_label.config(text='')
                self.description_date_label.config(text='')
            else:
                if ext=='pdf':
                    self.description_icon_label.config(image=self.pdf_file)
                    self.description_type_label.config(text=FILE_NAME[2])
                elif ext=='mp4' or ext=='avi' or ext=='mkv' or ext=='3gp'or ext=='webm':
                    self.description_icon_label.config(image=self.video_file)
                    self.description_type_label.config(text=FILE_NAME[3]) 
                elif ext=='zip' or ext=='rar'or ext=='tar'or ext=='gz':
                    self.description_icon_label.config(image=self.archive_folder)
                    self.description_type_label.config(text=FILE_NAME[4])
                elif ext=='mp3' or ext=='wav' or ext=='wma' or ext=='ogg' or ext=='m4a':
                    self.description_icon_label.config(image=self.music_file)
                    self.description_type_label.config(text=FILE_NAME[5])
                elif ext=='jpg' or ext=='jpeg' or ext=='png' or ext=='gif':
                    self.description_icon_label.config(image=self.picture)
                    self.description_type_label.config(text=FILE_NAME[6])
                elif ext=='lnk':
                    self.description_icon_label.config(image=self.link)
                    self.description_type_label.config(text=FILE_NAME[7])
                elif ext=='py' or ext=='pyc':
                    self.description_icon_label.config(image=self.python)
                    self.description_type_label.config(text=FILE_NAME[8])
                elif ext=='php':
                    self.description_icon_label.config(image=self.php)
                    self.description_type_label.config(text=FILE_NAME[9])
                elif ext=='pptm' or ext=='ppt':
                    self.description_icon_label.config(image=self.powerpoint)
                    self.description_type_label.config(text=FILE_NAME[10])
                elif ext=='html':
                    self.description_icon_label.config(image=self.html)
                    self.description_type_label.config(text=FILE_NAME[11])
                elif ext=='java' or ext=='jar' or ext=='class':
                    self.description_icon_label.config(image=self.java)
                    self.description_type_label.config(text=FILE_NAME[12])
                elif ext=='exe':
                    self.description_icon_label.config(image=self.exe)
                    self.description_type_label.config(text=FILE_NAME[13])
                elif ext=='xlsx' or ext=='csv':
                    self.description_icon_label.config(image=self.excel)
                    self.description_type_label.config(text=FILE_NAME[14])
                elif ext=='css':
                    self.description_icon_label.config(image=self.css)
                    self.description_type_label.config(text=FILE_NAME[15])
                elif ext=='cpp':
                    self.description_icon_label.config(image=self.cpp)
                    self.description_type_label.config(text=FILE_NAME[16])
                elif ext=='c':
                    self.description_icon_label.config(image=self.c)
                    self.description_type_label.config(text=FILE_NAME[17])
                elif ext=='doc' or ext=="docx" or ext=="odt":
                    self.description_icon_label.config(image=self.word)
                    self.description_type_label.config(text=FILE_NAME[18])
                elif ext=='txt':
                    self.description_icon_label.config(image=self.text)
                    self.description_type_label.config(text=FILE_NAME[19])
                elif ext=='crt':
                    self.description_icon_label.config(image=self.crt)
                    self.description_type_label.config(text=FILE_NAME[20])
                elif ext=='iso':
                    self.description_icon_label.config(image=self.disk_image)
                    self.description_type_label.config(text=FILE_NAME[21])
                elif ext=='dll':
                    self.description_icon_label.config(image=self.dll)
                    self.description_type_label.config(text=FILE_NAME[22])
                elif ext=='h':
                    self.description_icon_label.config(image=self.header)
                    self.description_type_label.config(text=FILE_NAME[23])
                elif ext=='htm':
                    self.description_icon_label.config(image=self.htm)
                    self.description_type_label.config(text=FILE_NAME[24])
                elif ext=='log':
                    self.description_icon_label.config(image=self.log)
                    self.description_type_label.config(text=FILE_NAME[25])
                elif ext=='perl':
                    self.description_icon_label.config(image=self.perl)
                    self.description_type_label.config(text=FILE_NAME[26])
                elif ext=='rpm':
                    self.description_icon_label.config(image=self.rpm)
                    self.description_type_label.config(text=FILE_NAME[27])
                elif ext=='rtf':
                    self.description_icon_label.config(image=self.rtf)
                    self.description_type_label.config(text=FILE_NAME[28])
                elif ext=='sql':
                    self.description_icon_label.config(image=self.sql)
                    self.description_type_label.config(text=FILE_NAME[29])
                elif ext=='xml':
                    self.description_icon_label.config(image=self.xml)
                    self.description_type_label.config(text=FILE_NAME[30])
                elif ext=='deb':
                    self.description_icon_label.config(image=self.deb)
                    self.description_type_label.config(text=FILE_NAME[31])
                else:
                    self.description_icon_label.config(image=self.other_file)
                    try:
                        if ext=='':
                            self.description_type_label.config(text=FILE_NAME[1])
                        else:
                            self.description_type_label.config(text='{0} {1}'.format(FILE_NAME[0],ext.upper()))
                    except AttributeError:
                        pass
                if FileModule.get_date(elmt) == None:
                    self.description_date_label.config(text='')
                if FileModule.get_size(elmt) == None:
                    self.description_size_label.config(text='')
                else:
                    self.description_date_label.config(text='{}'.format(FileModule.get_date(elmt)))
                    self.description_size_label.config(text='{0} : {1} Ko'.format(OTHERS_WORDS[1],FileModule.get_size(elmt)))   
        except TclError:
            pass

#------------------------------------------------------------------------------------------------
#----------------------------------[ MAIN PROGRAMM RUNNING... ]----------------------------------
#------------------------------------------------------------------------------------------------
py = PyAero()
py.main()