import os

import pytube
import ffmpeg


youtube_url = "https://www.youtube.com/watch?v=vjj16qog4vQ"

#youtube = pytube.YouTube( youtube_url )

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

#C:\Program Files\Tesseract-OCR;C:\MinGW\bin;C:\Users\Ballista\AppData\Local\Programs\Python\Python36\Scripts\;C:\Users\Ballista\AppData\Local\Programs\Python\Python36\;C:\ffmpeg-4.3.1\bin;C:\Program Files (x86)\MeCab\bin;C:\mysql\bin\;C:\Users\Ballista\AppData\Local\Programs\Python\Python38\Scripts\;C:\Users\Ballista\AppData\Local\Programs\Python\Python38\;C:\Users\Ballista\AppData\Local\atom\bin;C:\Program Files\Java\jdk-12.0.2;C:\mysql\bin;C:\xampp\php\;C:\Users\Ballista\composer;C:\Users\Ballista\AppData\Roaming\Composer\vendor\bin;C:\Program Files\heroku\bin;C:\Users\Ballista\AppData\Roaming\npm;C:\Users\Ballista\AppData\Local\GitHubDesktop\bin;C:\Users\Ballista\AppData\Local\Programs\Microsoft VS Code\bin

#format_list = pytube.YouTube( youtube_url ).streams.all()
#for format in format_list:
#    print( format.i )

#for item in youtube.streams.filter( file_extension='mp4', only_audio=True ).all():
#    print( item.itag )


from pytube import Playlist

# プレイリストのURLを入れてプレイリストを取得
p = Playlist( "https://youtube.com/playlist?list=PLHCf3kYa8R_n7yxq54HlKWwbLu0F8R0_-" )
p.length
for video in p.videos:
    print( video.title )
     #video.streams.first().download()
