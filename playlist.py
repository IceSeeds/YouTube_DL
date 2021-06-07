import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTTOM

import pytube
from pytube import Playlist

class List( tk.Frame ):
    def __init__( self, master, url, mode, title="Template", width=460, height=300 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        self.url = url
        self.mode = mode

        self.youtube = pytube.YouTube( url )
        
        self.data()
        self.create_widgets()
        self.insrt()

    def create_widgets( self ):
        self.my_tree = ttk.Treeview( self.master, height=20 )
        self.my_tree['columns'] = ( 1, 2, 3, 4, 5 )
        self.my_tree['show'] = "headings"
        self.my_tree.heading( 1, text="No." )
        self.my_tree.heading( 2, text="Title" )
        self.my_tree.heading( 3, text="not DL" )
        self.my_tree.heading( 4, text="movie" )
        self.my_tree.heading( 5, text="audio" )

        self.my_tree.column( 1, width=30 )
        self.my_tree.column( 2, width=220 )
        self.my_tree.column( 3, width=70 )
        self.my_tree.column( 4, width=70 )
        self.my_tree.column( 5, width=70 )

        self.my_tree.place( x=0, y=0 )

        self.radio = ttk.Radiobutton( master=self.my_tree, value="not" )

        for item, i in zip( self.play_list.videos, range( len( self.play_list ) ) ):
            self.my_tree.insert( parent="", index="end", values=( i, item.title ) )
        



        dl_run = ttk.Button( self.master, text="Download", command=self.callBack )
        dl_run.pack( side=BOTTOM )

    def callBack( self ):
        pass

    def insrt( self ):
        list = []
        radio_var = []
        for i in range( self.play_list_length ):
            array = []
            array.append( str( i ) + "_" + "not" )
            array.append( str( i ) + "_" + "movie" )
            array.append( str( i ) + "_" + "audio" )
            list.append( array )
            radio_var.append( tk.StringVar() )

        for items, i in zip( list, range( len( list ) ) ):
            for item, j in zip( items, range( len( items ) ) ):
                radio_d = ttk.Radiobutton( self.master, value=item, variable=radio_var[i] )
                radio_d.place( x = 50 * j + 290, y = 20 * i + 20 )

    def data( self ):
        self.play_list = Playlist( self.url )
        self.play_list_length = self.play_list.length

def main():
    root = tk.Tk()
    app = List( master=root, url="https://www.youtube.com/watch?v=XQ3HAOiqcA4&list=PLHCf3kYa8R_n7yxq54HlKWwbLu0F8R0_-&index=9", mode="mode" )
    app.mainloop()
    


if __name__ == "__main__":
    main()