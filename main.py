from tkinter import *
from tkinter import ttk
import classes.run as run

def main():
	#Configure tkinter GUI
	root = Tk()
	root.title("Speedy Boi Timekeeper")
	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)


	name = StringVar()
	splits = [StringVar()]
	goal = StringVar()
	newRun = run.RunData()

	name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
	name_entry.grid(column=2, row=1, sticky=(W, E))
	splits_entry = ttk.Entry(mainframe, width=7, textvariable=splits[0])
	splits_entry.grid(column=2, row=2, sticky=(W, E))
	goal_entry = ttk.Entry(mainframe, width=7, textvariable=goal)
	goal_entry.grid(column=2, row=3, sticky=(W, E))

	#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
	ttk.Button(mainframe, text="Create Config", command=lambda *args: newRun.createConfig(name, splits, goal)).grid(column=3, row=3, sticky=W)

	ttk.Label(mainframe, text="Name").grid(column=1, row=1, sticky=W)
	ttk.Label(mainframe, text="Splits").grid(column=1, row=2, sticky=E)
	ttk.Label(mainframe, text="Goal").grid(column=1, row=3, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	name_entry.focus()
	root.bind('<Return>', lambda *args: newRun.createConfig(name, splits, goal))
	root.mainloop()

if __name__ == '__main__':
    main()