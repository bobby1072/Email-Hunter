import tkinter as tk
import finder
def gui():
    window = tk.Tk()
    window.geometry("")
    window.title("email finder")
    tk.Label(
        window,
        text="please enter the url of the emails address's you want to find:"
    ).grid(row=0, sticky="w")
    key_ent = tk.Entry(window)
    key_ent.grid(row=0, column=1, sticky="w")
    def get_url():
        key = key_ent.get()
        heads = finder.mail_finder(key)
        if type(heads) == int:
            tk.Label(window, text="no emails found.").grid(row=2, sticky="w")
        elif len(heads) > 0:
            for i in range(0,len(heads)):
                tk.Label(window,text= heads[i]).grid(row=2 + i, sticky="w")
        else:
            tk.Label(window, text = "no emails found.").grid(row = 2, sticky = "w")
    tk.Button(text="search",command=get_url).grid(row=1, column=1)
    return window
if __name__ == "__main__":
    gui = gui()
    gui.mainloop()