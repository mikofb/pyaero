from tkinter import *
from tkinter import ttk
from pathlib import Path
import os, FileModule
import tkinter.messagebox

# Loading logo for the dialog box
icon = os.getcwd()+'/img/pyaero_logo.ico'

class Rename(Toplevel):
	"""
		This the class used to rename a folder or a file just with the real path
		@params file: the real path of the file or folder
	"""
	def __init__(self, file, params1, params2):
		super().__init__()
		self.params1 = params1
		self.params2 = params2
		self.title(self.params1[0])
		self.geometry('400x80+450+300')
		self.bind('<1w>Root')
		self.resizable(False, False)
		self.iconbitmap(bitmap=icon)
		self.config(bg = '#ebebeb')
		self.separator = Frame(self, bg='#b5b5b5', height=1)
		self.main_frame = Frame(self, bg = '#ebebeb')
		self.frame = Frame(self.main_frame, bg = '#ebebeb')
		self.new_name_entry = Entry(self.frame, font='Helvetica 11',bd= 2,  relief = FLAT, selectbackground="#10a4dc", highlightthickness=1, highlightcolor="#10a4dc", insertwidth=1)
		self.ok_button = Button(self, text=self.params1[0], relief = FLAT, border=0, bg="#10a4dc", command=self.excecute)
		self.cancel_button = Button(self, text=self.params1[1], relief = FLAT, border=0, bg="#10a4dc", command= self.close)
		self.separator.pack(side=TOP, fill=X)
		self.main_frame.pack(fill=BOTH)
		self.frame.pack(side = TOP, fill= BOTH)
		self.new_name_entry.pack(side = TOP, fill = X, padx=5, pady=5)
		self.cancel_button.pack(side = RIGHT, padx = 5)
		self.ok_button.pack(side = RIGHT)

		self.file = file
		self.new_name_entry.insert(0, "{}".format(os.path.split(self.file)[1]))
		self.new_name_entry.select_range(0,END)
		self.new_name_entry.focus_set()
		
		self.bind('<Escape>', self.close)
		self.new_name_entry.bind('<Return>', self.excecute)

	def excecute(self, *args):
		if self.new_name_entry.get() !='' and FileModule.checker(self.new_name_entry.get()):
			try:
				os.chdir(os.path.split(self.file)[0])
				if os.path.isdir(self.file):
					os.rename(os.path.split(self.file)[1], self.new_name_entry.get())
				elif os.path.isfile(self.file):
					try:
						if FileModule.get_file_extension(self.file) == FileModule.get_file_extension(self.new_name_entry.get()):
							os.rename(os.path.split(self.file)[1], self.new_name_entry.get())
						elif FileModule.get_file_extension(self.new_name_entry.get()) == '':
							os.rename(os.path.split(self.file)[1], self.new_name_entry.get()+'.'+FileModule.get_file_extension(self.file))
						else:
							req = tkinter.messagebox.askokcancel(self.params1[2],self.params1[3])
							if req:
								os.rename(os.path.split(self.file)[1], self.new_name_entry.get())
					except PermissionError:
						tkinter.messagebox.showerror(self.params2[0], self.params2[1])
				else:
					pass
				self.close()
			except FileExistsError:
				tkinter.messagebox.showerror(self.params2[2], self.params2[3])

	def close(self, *args):
		self.destroy()

class New(Toplevel):
	"""
		This the class used to create a new folder or a new file in the current directory
	"""
	def __init__(self, path, params1, params2):
		super().__init__()
		self.params1 = params1
		self.params2 = params2
		self.title(self.params1[0])
		self.geometry('400x100+450+300')
		self.bind('<1w>Root')
		self.resizable(False, False)
		self.iconbitmap(bitmap=icon)
		self.typ_folder = IntVar()
		self.typ_file = IntVar()
		self.separator = Frame(self, bg='#b5b5b5', height=1)
		self.main_frame = Frame(self, bg = '#ebebeb')
		self.frame = Frame(self.main_frame, bg = '#ebebeb')
		self.rad_frame = Frame(self.main_frame, bg = '#ebebeb')
		self.folder_radio = Checkbutton(self.rad_frame, text=self.params1[2], variable=self.typ_folder, bg = '#ebebeb', relief = FLAT, font='Helvetica 9', offrelief=FLAT)
		self.file_radio = Checkbutton(self.rad_frame, text=self.params1[1], variable=self.typ_file, bg = '#ebebeb', relief = FLAT, font='Helvetica 9', offrelief=FLAT)
		self.new_name_entry = Entry(self.frame, font='Helvetica 11',bd= 2,  relief = FLAT, highlightthickness=1, highlightcolor="#10a4dc", insertwidth=1)
		self.ok_button = Button(self, text=self.params1[3], relief = FLAT, border=0, bg="#10a4dc", command=self.excecute)
		self.cancel_button = Button(self, text=self.params1[4], relief = FLAT, border=0, bg="#10a4dc", command= self.close)
		
		self.separator.pack(side=TOP, fill=X)
		self.main_frame.pack(fill=BOTH)
		self.rad_frame.pack(side=TOP, fill=X)
		self.folder_radio.pack(side=RIGHT)
		self.file_radio.pack(side=RIGHT)
		self.frame.pack(side = TOP, fill= BOTH)
		self.new_name_entry.pack(side = TOP, fill = X, padx=5, pady=5)
		self.cancel_button.pack(side = RIGHT, padx = 5)
		self.ok_button.pack(side = RIGHT)
		self.file = path
		
		self.config(bg = '#ebebeb')
		self.new_name_entry.focus_set()

		self.bind('<Escape>', self.close)
		self.new_name_entry.bind('<Return>', self.excecute)

	def excecute(self, *args):
		if self.new_name_entry.get() != '' and FileModule.checker(self.new_name_entry.get()):
			if self.typ_folder.get() == 1 and self.typ_file.get() == 0:
				os.chdir(self.file)
				try:
					os.mkdir('{}'.format(self.new_name_entry.get()))
				except FileExistsError:
					tkinter.messagebox.showerror(self.params2[2],self.params2[3])
			elif self.typ_file.get() == 1 and self.typ_folder.get() ==0:
				os.chdir(self.file)
				open('{}'.format(self.new_name_entry.get()),'a').close()
			else:
				pass
			self.close()

	def close(self, *args):
		self.destroy()

class Delete(Toplevel):
	"""
		This the class used to delete a folder or a file just with the real path
		@params file: the real path of the file or folder
	"""
	def __init__(self, file, params1, params2):
		super().__init__()
		self.params1 = params1
		self.params2 = params2
		self.title(self.params1[0])
		self.geometry('400x80+450+300')
		self.bind('<1w>Root')
		self.resizable(False, False)
		self.iconbitmap(bitmap=icon)
		self.top_sep = Frame(self, bg='#b5b5b5', height=1)
		self.main_frame = Frame(self, bg = '#ebebeb')
		self.info_label = Label(self.main_frame, text=self.params1[3], bg = '#ebebeb', relief = FLAT, font='Helvetica 9')
		self.ok_button = Button(self, text=self.params1[1], relief = FLAT, border=0, bg="#10a4dc", command=self.excecute)
		self.cancel_button = Button(self, text=self.params1[2], relief = FLAT, border=0, bg="#10a4dc", command= self.close)
		self.top_sep.pack(side=TOP, fill=X)
		self.main_frame.pack(fill=BOTH)
		self.info_label.pack(side = LEFT, pady=5)
		self.cancel_button.pack(side = RIGHT, padx = 5)
		self.ok_button.pack(side = RIGHT)
		self.elmt = file
		self.config(bg = '#ebebeb')
		self.bind('<Escape>', self.close)
		self.ok_button.bind('<Return>', self.excecute)

	def excecute(self, *args):
		try:
			FileModule.delete_file(self.elmt)
		except PermissionError:
			tkinter.messagebox.showerror(self.params2[0], self.params2[1]) 
		finally:
			pass
		self.close()

	def close(self, *args):
		self.destroy()

class Properties(Toplevel):
	"""
		This the class used to dispay the properties of a folder or a file just with the real path
		@params file: the real path of the file or folder
	"""
	def __init__(self, name, file):
		super().__init__()
		self.title('{0} : {1}'.format(name[0], file))
		self.geometry('500x400+450+200')
		self.bind('<1w>Root')
		self.resizable(False, False)
		self.iconbitmap(bitmap=icon)
		self.config(bg='#ebebeb')
		self.file = file
		self.main_frame = Frame(self, bg='white', border=0, relief=FLAT)
		
		self.frame1 = Frame(self.main_frame, bg='white', border=0, relief=FLAT)
		self.entry = Entry(self.frame1, width=50, relief=FLAT)
		self.sep1 = Frame(self.main_frame, bg='#b5b5b5', height=1, relief=FLAT)
		
		self.frame2 = Frame(self.main_frame, bg='white', border=0, relief=FLAT)
		self.type = Label(self.frame2, text = 'Type      : {}'.format(4*5), anchor='nw', relief=FLAT)
		self.exts = Label(self.frame2, text = 'Extension : {}'.format(5-6), anchor='nw', relief=FLAT)
		self.sep2 = Frame(self.main_frame, bg='#b5b5b5', height=1, relief=FLAT)
		
		self.frame3 = Frame(self.main_frame, bg='white', border=0, relief=FLAT)
		self.path = Label(self.frame3, text = 'Emplacement : {}'.format(5-6), anchor='nw', relief=FLAT)
		self.size = Label(self.frame3, text = 'Taille      : {}'.format(5-6), anchor='nw', relief=FLAT)
		self.sep3 = Frame(self.main_frame, bg='#b5b5b5', height=1, relief=FLAT)
		
		self.frame4 = Frame(self.main_frame, bg='white', border=0, relief=FLAT)
		self.date = Label(self.frame4, text = 'Date de modification : {}'.format(5-6), anchor='nw', relief=FLAT)
		
		self.ok_button = Button(self, text = 'Ok', relief = FLAT, bg="#10a4dc", command=self.close)
		
		self.main_frame.pack(fill=BOTH, padx=5, pady=5)
		self.frame1.pack(side=TOP)
		self.sep1.pack(side=TOP, padx = 5, pady = 2, fill=X)
		self.frame2.pack(side=TOP)
		self.type.pack(side=TOP)
		self.exts.pack(side=TOP)
		self.sep2.pack(side=TOP, padx = 5, pady = 2, fill=X)
		self.frame3.pack(side=TOP)
		self.path.pack(side=TOP)
		self.size.pack(side=TOP)
		self.sep3.pack(side=TOP, padx = 5, pady = 2, fill=X)
		self.frame4.pack(side=TOP)
		self.date.pack(side=TOP)

	def close(self):
		self.destroy()

class Settings(Toplevel):
	"""docstring for ClassName"""
	def __init__(self,name):
		super().__init__()
		self.title(name)
		self.geometry('500x400+450+200')
		self.bind('<1w>Root')
		self.resizable(False, False)
		self.iconbitmap(bitmap=icon)
		self.config(bg='#ebebeb')

class About(Toplevel):
	"""docstring for About"""
	def __init__(self, name):
		super().__init__()
		self.title(name)
		self.geometry('500x400+450+200')
		self.bind('<1w>Root')
		self.resizable(False, False)
		self.iconbitmap(bitmap=icon)
		self.config(bg='#ebebeb')
		

		