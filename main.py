import os

import pytube
import ffmpeg


youtube_url = "https://www.youtube.com/watch?v=vjj16qog4vQ"

youtube = pytube.YouTube( youtube_url )

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

for item in youtube.streams.filter( file_extension='mp4', only_audio=True ).all():
    print( item.itag )
