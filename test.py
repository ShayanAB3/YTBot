from public.api.yt_dlp.yt_dlp import YTDlp

OPTIONS_YTDLP = {
    'extract_flat': True,
    'noplaylist': True,
    'writesubtitles':False
}
yt_dlp_instance = YTDlp()
search_results = yt_dlp_instance.search_or_url("Dark is the Night - Soviet WW2 Song")
print(search_results)