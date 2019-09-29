from tkinter import *
import tkinter.filedialog
from tkinter import messagebox


class Text_Editor:
	@staticmethod
	def quit_app(event=None):
		root.quit()
		
	def open_file(self, event = None):
			txt_file = tkinter.filedialog.askopenfilename(parent=root, initialdir='/User/mydir')
			if txt_file:
				self.text_area.delete('1.0', END)
				with open(txt_file)as file:
					self.text_area.insert('1.0', file.read())
					root.update_idletasks()
	
	def change_font(event=None):
		print("font picked: ")
		
	def save_file(self, event = None):
		file = tkinter.filedialog.asksaveasfile(mode='w')
		if file != None:
			data=self.text_area.get('1.0', END+'-1c')
			file.write(data)
			file.close()
	@staticmethod
	def show_about(event=None):
		messagebox.showwarning("About", "Umar's program")
		
	def __init__(self, root):
		self.text_to_write = " "
		root.title("Umar'sText Editor")
		root.geometry("800x600")
		frame = Frame(root, width=800, height=600)
		scrollbar = Scrollbar(frame)
	
		self.text_area = Text(frame, width=100, height=90, yscrollcommand=scrollbar.set, padx=10, pady=10)
		scrollbar.config(command=self.text_area.yview)
		scrollbar.pack(side="right", fill="y")
		self.text_area.pack(side="left", fill="both", expand=True)
		frame.pack()
		the_menu = Menu(root)
		file_menu = Menu(the_menu, tearoff=0)
		file_menu.add_command(label="open", command=self.open_file)
		file_menu.add_command(label="save", command=self.save_file)
		file_menu.add_command(label="Quit", command=self.quit_app)
		file_menu.add_separator()
		the_menu.add_cascade(label="file", menu=file_menu)
	
		text_font = StringVar()
		text_font.set("Times")
		view_menu = Menu(the_menu, tearoff=0)
		line_numbers = IntVar()
		line_numbers.set(1)
		view_menu.add_checkbutton(label="linenumbers", variable=line_numbers)
		
		font_menu = Menu(the_menu, tearoff=0)
		font_menu.add_radiobutton(label = "Times", variable=text_font)
		font_menu.add_radiobutton(label="courier", variable=text_font)
		font_menu.add_radiobutton(label="ariel", variable=text_font)
		view_menu.add_cascade(label="fonts", menu=font_menu)
		the_menu.add_cascade(label="view", menu=view_menu)
		help_menu = Menu(the_menu, tearoff=0)
		help_menu.add_command(label="About", command=self.show_about)
		the_menu.add_cascade(label="details", menu=help_menu)
		root.config(menu=the_menu)
		
		
root = Tk()
text_editor = Text_Editor(root)
root.mainloop()
