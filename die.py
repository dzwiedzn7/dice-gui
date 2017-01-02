# coding: utf-8

import random
import Tkinter as tk


class Model(object):

    def __init__(self):
        self.__value = None
        self.__f = None

    @property
    def value(self):
        return self.__value

    def reroll(self):
        self.__value = random.randint(1, 6)
        self.on_reroll(self.__value)

    def on_reroll(self, value):
        if not callable(self.__f):
            return
        self.__f(value)

    def unset_reroll_callback(self):
        self.set_reroll_callback(None)

    def set_reroll_callback(self, f):
        self.__f = f


class App(tk.Frame):

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack()

        self.__model = Model()
        self.__model.set_reroll_callback(self.sync_label)

        self.__button = tk.Button(self)
        self.__button["text"] = "Reroll"
        self.__button["command"] = self.on_reroll
        self.__button.pack({"side": "left"})

        self.__label = tk.Label(self)
        self.sync_label(None)
        self.__label.pack({"side": "right"})

    def on_reroll(self):
        self.__model.reroll()

    def sync_label(self, value):
        if value is None:
            text = "No result yet"
        else:
            text = str(value)

        self.__label["text"] = text


if __name__ == '__main__':
    root = tk.Tk()
    app = App(parent=root)
    app.mainloop()
