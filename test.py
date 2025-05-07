<<<<<<< HEAD
#from public.orm.session import session
#from public.orm.models.playlist import Playlist
#from public.orm.models.track import Track

#from sqlalchemy import func 
#playlists = session.query(Playlist).all()
#for playlist in playlists:
#    print(playlist.name)

#tracks_with_playlist = session.query(Track).join(Track.playlist).all()

#playlists = session.query(Track).filter_by(server_id=1048228124292300800,playlist_id=4).all()
#for playlist in playlists:
#    print(playlist.title)

#playlists:list[Playlist] = session.query(Playlist.author_id,func.json_arrayagg(Playlist.name).label("names_json"),Playlist.server_id).group_by(Playlist.author_id,Playlist.server_id).filter_by(server_id=1048228124292300800)

#tracks = session.query(Playlist).filter_by(server_id=1048228124292300800)
#for playlist in playlists:
#    print(playlist.names_json)
#for track in tracks_with_playlist:
#    print(track.title, "->", track.playlist.name)

#playlist = session.get(Playlist,1)
#print(playlist.name)

#playlist = session.query(Playlist).filter_by(name="Мой плейлист 1").first()
#if playlist:
#    playlist.name = "Мой плейлист 1"
#    session.commit()

#if playlist:
#    session.delete(playlist)
#    session.commit()



from yt_dlp import YoutubeDL
import pyperclip

#url = "https://www.youtube.com/playlist?list=PLHiq9KhznxD3qFnb7ppgzOxZ1OJaTiD0e"
#
## Опции yt-dlp
#ydl_opts = {
#    'quiet': True,
#    'extract_flat': True,
#    'skip_download': True
#}

#with YoutubeDL(ydl_opts) as ydl:
#    info = ydl.extract_info(url, download=False)
#    pyperclip.copy(info)


url = "https://www.youtube.com/watch?v=lrv0AAmzltw&list=RDMMbXgMi2ySIP0"

ydl_opts = {
    'cookiefile': 'cookies.txt',
    'extract_flat': True,
    'skip_download': True
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    pyperclip.copy(info)
=======
from public.api.yt_dlp.yt_dlp import YTDlp

OPTIONS_YTDLP = {
    'extract_flat': True,
    'noplaylist': True,
    'writesubtitles':False
}
yt_dlp_instance = YTDlp()
search_results = yt_dlp_instance.search_or_url("Dark is the Night - Soviet WW2 Song")
print(search_results)
>>>>>>> 1fbe3886b2dd00b21d73aafabe7f66cc74526607
