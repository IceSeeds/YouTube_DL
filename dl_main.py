import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, TOP

import list

class Application( tk.Frame ):
    def __init__( self, master, title="Youtube_Download  Ver 2.0", width=300, height=150 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        self.create_widgets()

    def create_widgets( self ):
        self.l_youtube_url = ttk.Label( master=self.master, text="Youtube URL" )
        self.l_youtube_url.pack( side=TOP )

        self.youtube_url = ttk.Entry( master=self.master, width=250, text="https://www.youtube.com/watch?v=vjj16qog4vQ" )
        self.youtube_url.pack( side=TOP )

        self.radio()

        self.run = ttk.Button( master=self.master, text="Run", command=self.callBack )
        self.run.pack( side=BOTTOM )

    def radio( self ):
        self.str_var = StringVar( value="all" )

        self.all = ttk.Radiobutton( master=self.master, text="all", value="all", variable=self.str_var )
        self.all.place( x=20, y=70 )
        self.movie = ttk.Radiobutton( master=self.master, text="movie", value="movie", variable=self.str_var )
        self.movie.place( x=110, y=70 )
        self.audio = ttk.Radiobutton( master=self.master, text="audio", value="audio", variable=self.str_var )
        self.audio.place( x=220, y=70 )

    def callBack( self ):
        #self.youtube_url.get()
        youtube_url = self.youtube_url.get()
        radio_get = self.str_var.get()
        
        self.new_window( youtube_url, radio_get )
        
    def new_window( self, data, mode ):
        self.newWindow = tk.Toplevel( self.master )
        self.app2 = list.List( self.newWindow, data, mode )

def main():
    root = tk.Tk()
    app = Application( master=root )
    app.mainloop()
    


#if __name__ == "__main__":
main()


#ffmpeg-python 映像と音声の結合
#https://blog.syoukannoyakata.com/?p=205
#