import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, TOP

import single, playlist

class Application( tk.Frame ):
    def __init__( self, master, title="Youtube_Download  Ver 2.3", width=300, height=150 ):
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

        self.playlist_or_single()
        self.radio()

        self.run = ttk.Button( master=self.master, text="Run", command=self.callBack )
        self.run.pack( side=BOTTOM )

    def playlist_or_single( self ):
        
        self.str_var_play = StringVar( value="single" )

        self.single = ttk.Radiobutton( master=self.master, text="single", value="single", variable=self.str_var_play )
        self.single.place( x=50, y=55 )
        self.playlist = ttk.Radiobutton( master=self.master, text="playlist", value="playlist", variable=self.str_var_play )
        self.playlist.place( x=180, y=55 )
        
    def radio( self ):
        self.str_var = StringVar( value="all" )

        self.all = ttk.Radiobutton( master=self.master, text="all", value="all", variable=self.str_var )
        self.all.place( x=20, y=90 )
        self.movie = ttk.Radiobutton( master=self.master, text="movie", value="movie", variable=self.str_var )
        self.movie.place( x=110, y=90 )
        self.audio = ttk.Radiobutton( master=self.master, text="audio", value="audio", variable=self.str_var )
        self.audio.place( x=220, y=90 )

    def callBack( self ):
        #self.youtube_url.get()
        youtube_url = self.youtube_url.get()
        radio_get = self.str_var.get()

        list_or_single = self.str_var_play.get()
        if list_or_single == "single":
            self.new_window( youtube_url, radio_get )
        else:
            self.new_playlist( youtube_url, radio_get )

    def new_playlist( self, url, mode ):
        self.newWindow = tk.Toplevel( self.master )
        self.app2 = playlist.List( self.newWindow, url, mode )

    def new_window( self, data, mode ):
        self.newWindow = tk.Toplevel( self.master )
        self.app2 = single.Single( self.newWindow, data, mode )

def main():
    root = tk.Tk()
    app = Application( master=root )
    app.mainloop()
    


#if __name__ == "__main__":
main()


#ffmpeg-python 映像と音声の結合
#https://blog.syoukannoyakata.com/?p=205
#