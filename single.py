import os

import tkinter as tk
from tkinter import Button, ttk
from tkinter.constants import BOTTOM
import tkinter.messagebox as messagebox

import pytube
import ffmpeg
from pytube.__main__ import YouTube


class Single( tk.Frame ):
    def __init__( self, master, list_data, mode="all", title="LIST", width=720, height=400 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        self.out_folder = os.getcwd() + "\\out_folder\\"
        self.temp_video = "temp_video"
        self.temp_audio = "temp_audio"

        self.mode = mode
        print( self.mode )
        self.list_data = list_data
        self.youtube = pytube.YouTube( self.list_data )

        self.select_list = ""

        self.create_widgets()

    def create_widgets( self ):
        self.my_tree = ttk.Treeview( self.master, height=20 )
        self.my_tree['columns'] = ( 1, 2, 3, 4, 5, 6 )
        self.my_tree['show'] = "headings"
        self.my_tree.heading( 1, text="type" )
        self.my_tree.heading( 2, text="res" )
        self.my_tree.heading( 3, text="fps" )
        self.my_tree.heading( 4, text="code" )
        self.my_tree.heading( 5, text="mine_type" )
        self.my_tree.heading( 6, text="itag" )

        self.my_tree.column( 1, width=120 )
        self.my_tree.column( 2, width=120 )
        self.my_tree.column( 3, width=120 )
        self.my_tree.column( 4, width=120 )
        self.my_tree.column( 5, width=120 )
        self.my_tree.column( 6, width=120 )

        self.mode_list()

        self.my_tree.place( x=0, y=0 )

        dl_run = ttk.Button( self.master, text="Download", command=self.callBack )
        dl_run.pack( side=BOTTOM )

    def mode_list( self ):
        format_list = None
        if self.mode == "all":
            format_list = pytube.YouTube( self.list_data ).streams.all()
        elif self.mode == "movie":
            format_list = pytube.YouTube( self.list_data ).streams.filter( file_extension='mp4', only_video=True ).all()
        else:
            format_list = pytube.YouTube( self.list_data ).streams.filter( file_extension='mp4', only_audio=True ).all()

        for item in format_list:
            codec = ""
            if item.video_codec is None:
                codec = item.audio_codec
            else:
                codec = item.video_codec
            
            res = ""
            if item.resolution is None:
                res = item.abr
            else:
                res = item.resolution
            
            self.my_tree.insert( parent="", index="end", values=( item.type, res, item.fps, codec, item.mime_type, item.itag ) )
            self.my_tree.bind("<<TreeviewSelect>>", self.on_tree_select )

    def on_tree_select( self, event ):
        #print("selected items:")
        for item in self.my_tree.selection():
            self.item_text = self.my_tree.set( item )
            self.select_list = self.item_text
            #print( self.select_list )
    
    def callBack( self ):
        ret = messagebox.askyesno( "confirmation", "以下の情報でDownloadしまか？\n【" + str( self.item_text ) + "】" )
        if ret == True:
            print( "Start ~ ", self.file_name_variable( self.youtube.title ) , " ~" )

            #dl_title = self.file_name_variable( self.youtube.title )
            if self.mode == "movie":
                dl_title = self.temp_video
            elif self.mode == "audio":
                dl_title = self.temp_audio
            else:
                dl_title = self.file_name_variable( self.youtube.title )

            itag = self.select_list["6"]
            self.youtube.streams.get_by_itag( itag ).download( filename=dl_title, output_path=os.path.abspath( "out_folder" ) )
            if "audio/mp4" in self.item_text["5"]:
                self.mp4_to_mp3( dl_title )
        
            if self.mode == "movie":
                self.select_movie()

            print( "Finish ~ ", self.file_name_variable( self.youtube.title ) ," ~" )
            
    def mp4_to_mp3( self, file_name ):
        stream = ffmpeg.input( self.out_folder + file_name + ".mp4" )# 入力
        stream = ffmpeg.output( stream, self.out_folder + file_name + ".mp3" )# 出力
        ffmpeg.run( stream )# 実行

        os.remove( self.out_folder + file_name + ".mp4" )

        if self.mode == "audio":
            os.rename( self.out_folder + file_name + ".mp3", self.out_folder + self.file_name_variable( self.youtube.title ) + ".mp3" )
    
    def file_name_variable( self, name ):
        name = name.replace( "\\", "" )
        name = name.replace( "/", "" )
        name = name.replace( ":", "" )
        name = name.replace( "*", "" )
        name = name.replace( "?", "" )
        name = name.replace( "\"", "" )
        name = name.replace( "<", "" )
        name = name.replace( ">", "" )
        name = name.replace( "|", "" )

        return name

    def select_movie( self ):
        self.only_audio()
        self.video_in_audio()

    def only_audio( self ):
        for item in self.youtube.streams.filter( file_extension='mp4', only_audio=True ).all():
            #dl_title = self.file_name_variable( self.youtube.title ) + "_audio"

            self.youtube.streams.get_by_itag( item.itag ).download( filename=self.temp_audio, output_path=os.path.abspath( "out_folder" ) )
            self.mp4_to_mp3( self.temp_audio )

        
    def video_in_audio( self ):
        instream_v = ffmpeg.input( self.out_folder + self.temp_video + ".mp4" )#映像の読み込み
        instream_a = ffmpeg.input( self.out_folder + self.temp_audio + ".mp3" )#音声の読み込み

        #コーデックと出力ファイルの指定
        stream = ffmpeg.output( instream_v, instream_a, self.out_folder + self.file_name_variable( self.youtube.title ) + ".mp4", vcodec="copy", acodec="copy" )
        
        ffmpeg.run( stream )#実行

        os.remove( self.out_folder + self.temp_video + ".mp4" )
        os.remove( self.out_folder + self.temp_audio + ".mp3" )
