from tkinter import (
    RIGHT,
    Button,
    Label,
    LEFT,
    Entry,
    Menu,
    Scale,
    HORIZONTAL,
    #  Toplevel,
    IntVar,
    Checkbutton,
    Tk,
    #  filedialog,
    messagebox,
)

label_settings = {"font": ("Arial", 25), "borderwidth": "10", "background": "lightblue"}


class Settings(object):
    def __init__(self, el_num, el_dist, volts, current, frequency):
        self.el_num = el_num
        self.el_dist = el_dist
        self.volts = volts
        self.current = current
        self.frequency = frequency


# Main Settings
settings_upd = Settings(0, 0, 0, 0, 0)

"""
funcions
"""


def set_n_el():
    settings_upd.el_num = el_num.get()
    print(settings_upd.__dict__)
    update_EL_DIST()


def update_EL_DIST():
    EL_DIST = Scale(
        app,
        from_=0,
        to=el_num.get(),
        orient=HORIZONTAL,
        background="white",
        command=set_el_dist,
    )
    EL_DIST.grid(column=1, row=3, columnspan=4, **grid_dict)
    EL_DIST["state"] = "normal"


def set_el_dist(val):
    settings_upd.el_dist = val


def set_volts():
    settings_upd.volts = VOLTS.get()
    VOLTS_b.configure(bg="green", fg="white")
    print(settings_upd.__dict__)


def set_frequency():
    settings_upd.frequency = FREQ.get()
    FREQ_b.configure(bg="green", fg="white")
    print(settings_upd.__dict__)


def set_current():
    settings_upd.current = CURRENT.get()
    CURRENT_b.configure(bg="green", fg="white")
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


"""
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

"""
functions end
"""

app = Tk()
app.title("EIT measurenment user interface")
app.configure(background="white")
app.grid()

Label(app, text="Settings for measurement", **label_settings).grid(
    columnspan=5, ipadx=200, ipady=5
)

"""
Checklist
"""
grid_dict = {"sticky": "w", "ipadx": "10"}

# el_num
Label(
    app,
    justify=LEFT,
    padx=10,
    text="Number of electrodes:\t",
    background="white",
    border=10,
).grid(row=2, **grid_dict)
el_num = IntVar()
el_vals = [16, 32, 64, 128]

for clm, evals in enumerate(el_vals):
    Checkbutton(
        app,
        text=str(evals) + "\t",
        onvalue=evals,
        offvalue=0,
        variable=el_num,
        command=set_n_el,
        background="white",
    ).grid(row=2, column=clm + 1)


# el_dist

EL_DIST = Label(
    app,
    justify=LEFT,
    padx=10,
    text="Electrode distance:\t",
    border=10,
)
EL_DIST.grid(row=3, **grid_dict)

EL_DIST = Scale(
    app,
    from_=0,
    to=settings_upd.el_num,
    orient=HORIZONTAL,
    background="white",
    command=set_el_dist,
)

EL_DIST.grid(column=1, row=3, columnspan=4, **grid_dict)
# enable, if el_num is selected
EL_DIST["state"] = "disabled"

# volts
Label(
    app,
    justify=LEFT,
    padx=10,
    text="Voltage:\t",
    background="white",
    border=10,
).grid(row=4, **grid_dict)

VOLTS = Entry(app, width=8)
VOLTS.grid(row=4, column=1)
Label(app, justify=RIGHT, text="[mV]").grid(row=4, column=1, sticky="e")

VOLTS_b = Button(app, text="set", command=set_volts)
VOLTS_b.grid(row=4, column=2)
#  current #row=5
Label(
    app,
    justify=LEFT,
    padx=10,
    text="Current: \t \t",
    border=10,
).grid(row=5, **grid_dict)

CURRENT = Entry(app, width=8)
CURRENT.grid(row=5, column=1)
Label(app, justify=RIGHT, text="[mA]").grid(row=5, column=1, sticky="e")

CURRENT_b = Button(app, text="set", command=set_current)
CURRENT_b.grid(row=5, column=2)
#  frequency # row=6
Label(
    app,
    justify=LEFT,
    padx=10,
    text="Frequency:\t",
    background="white",
    border=10,
).grid(row=6, **grid_dict)

FREQ = Entry(app, width=8)
FREQ.grid(row=6, column=1)
Label(app, justify=RIGHT, text="[HZ]").grid(row=6, column=1, sticky="e")

FREQ_b = Button(app, text="set", command=set_frequency)
FREQ_b.grid(row=6, column=2)

" Submit"


def changeText():
    if sub_button["text"] == "Saved":
        sub_button["text"] = "Save"
        sub_button.configure(bg="grey", fg="black")
        button_action()
    else:
        sub_button["text"] = "Saved"
        sub_button.configure(bg="green", fg="white")
        button_action()


sub_button = Button(app, text="Save", command=changeText)
sub_button.grid(row=7, column=4)


# Menüleiste erstellen
dropdown = Menu(app)
# Menü File Help erstellen
datei_menu = Menu(dropdown, tearoff=0)
help_menu = Menu(dropdown, tearoff=0)
# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Run", command=button_action)
datei_menu.add_command(label="Save settings")  # , command=save_window
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
