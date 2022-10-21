from ast import Str
from sqlite3 import Row
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from turtle import color, left

label_settings = {"font": "15", "background": "white"}
pack_settings = {"pady": "10", "side": "top", "anchor": "n"}
grid_settings = {"pady": "10", "sticky": "n"}
box_pack = {"pady": 20, "side": "left", "anchor": "ne"}
spath = ""


class Settings(object):
    def __init__(self, el_num, el_dist, volts, current, frequency):
        self.el_num = el_num
        self.el_dist = el_dist
        self.volts = volts
        self.current = current
        self.frequency = frequency


# Main Settings
settings_upd = Settings(128, "", 10, 0.1, 0)


"""
funcions
"""


def displayinput():
    settings_upd.el_num = el_num.get()
    # settings_upd.el_dist = el_dist.get()
    print(settings_upd.__dict__)


def button_action():
    print("Aktuellen Settings:\n", settings_upd.__dict__)


def action_get_info_dialog():
    m_text = "\
************************\n\
Autor: Jacob Thönes\n\
Date: Oktober 2022\n\
Version: 1.00\n\
Contct: jacob.thoenes@uni-rostock.de \n\
************************"
    messagebox.showinfo(message=m_text, title="Info")


def save_window():

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(app)
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    spath = filedialog.askopenfilename(
        initialdir="/",
        title="Select a save path",
        # filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )
    # A Label widget to show in toplevel
    Label(newWindow, text="This is a new window").pack()


"""
functions end
"""

app = Tk()
app.title("EIT measurenment user interface")

app.grid()

row = 2
print(row)

Label(app, text="Checklist for measurement", **label_settings).grid(row=0)

# el_num
Label(
    app, justify=LEFT, padx=10, text="Number of electrodes:\t", background="red",
).grid(row=row, sticky="w")
el_num = IntVar()
el_vals = [16, 32, 64, 128]

for clm, evals in enumerate(el_vals):
    Checkbutton(
        app,
        text=str(evals) + "\t",
        onvalue=evals,
        offvalue=0,
        variable=el_num,
        command=displayinput,
        background="blue",
    ).grid(row=row, column=clm + 1)


# el_dist
EL_DIST = Label(app, justify=LEFT, padx=10, text="Electrode distance")
EL_DIST.grid(row=15, sticky="w")
# EL_DIST.pack(**box_pack)
# el_dist = IntVar()
"""
EL_DIST = Scale(
    app,
    from_=0,
    to=el_num.get(),
    orient=HORIZONTAL,
    variable=el_dist,
    command=displayinput,
)
EL_DIST.pack(**box_pack)
# volts
"""
#  current

#  frequency


def changeText():
    if sub_button["text"] == "Submitted":
        sub_button["text"] = "Submit"
    else:
        sub_button["text"] = "Submitted"


sub_button = Button(app, text="Submit", command=changeText)
sub_button.grid(sticky="se")


# Menüleiste erstellen
dropdown = Menu(app)
# Menü File Help erstellen
datei_menu = Menu(dropdown, tearoff=0)
help_menu = Menu(dropdown, tearoff=0)
# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Run", command=button_action)
datei_menu.add_command(label="Save settings", command=save_window)
datei_menu.add_separator()  # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Exit", command=app.quit)

help_menu.add_command(label="Info", command=action_get_info_dialog)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
dropdown.add_cascade(label="File", menu=datei_menu)
dropdown.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem app übergeben und fertig.
app.config(menu=dropdown)

app.geometry("800x400")

app.mainloop()
