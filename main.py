import os

import pytube
import ffmpeg


youtube_url = "https://www.youtube.com/watch?v=qchY7kNcLi4"
#pytube.YouTube( youtube_url ).streams.first().download()
youtube = pytube.YouTube( youtube_url )
format_list = youtube.streams.filter( file_extension='mp4', only_audio=True ).all()
print( format_list )
#youtube.streams.filter( file_extension='mp4', only_audio=True )
#dl_title = youtube.title.replace( ".", "" )

#print( os.path.abspath( "out_folder" ) )
#dl_itag = youtube.streams.get_by_itag( 140 ).download( filename=dl_title, output_path=os.path.abspath( "out_folder" ) )
#ret = youtube.streams.get_by_itag( 140 ).on_progress()
#print( ret )
#dl_high = youtube.streams.get_highest_resolution()
#print( dl_high["itag"] )

#stream = ffmpeg.input( dl_title + ".mp4" )# 入力
#stream = ffmpeg.output( stream, dl_title + ".mp3" )# 出力
#ffmpeg.run( stream )# 実行

#os.remove( dl_title + ".mp4" )



#format_list = pytube.YouTube( youtube_url ).streams.all()
#for format in format_list:
#    print( format.i )

#for item in youtube.streams.filter( file_extension='mp4', only_audio=True ).all():
#    print( item.itag )

"""
import youtube_dl
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download( ['https://www.youtube.com/watch?v=qchY7kNcLi4'] )
    ydl.list_formats()
"""