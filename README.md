# YTBot
This is a music bot for playing YouTube music. There are several commands to control the bot.
Let me remind you that all commands are controlled by slash-commands.

## What dependencies are needed to run the bot?
1. Make .env file and write:
> TOKEN=`token`
> COMMAND_PREFIX=`prefix`
> STORAGE_DIR=storage

2. Install ffmpeg
[Link for installing ffmpeg](https://www.ffmpeg.org/)
To check that you have installed ffmpeg, enter the command: `ffmpeg -version`

3. Install libraly
To install libraries, use the `requirements.txt` file. Command: `pip install -r /path/to/requirements.txt`

4. Run MySQL
Once you have started the database, create the database and load the database dump. For database configurations, fill the .env file with these values.
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASS=

## Commands:
### join
> Join voice channel
### leave
> Leave voice channel
### play :name_or_url
> The command is for playing music and takes an argument the name or link of the music.
### pause
> Pauses music playback.
### resume
> Play pausing music.
### stop
> Stops music playback and clears the queue of further played music.
### next
> Skips the current music and switches to the next one.
### show_queue
> Shows a list of the next playing music.
### now_play
> Shows the currently playing song.
### playlist :playlist
> Adds tracks from the playlist to the play queue.


## Commands for manage playlists:
### public-playlist-manage create :playlist
> Create playlist
### public-playlist-manage update :playlist :update_to
> Update playlist name
### public-playlist-manage delete :playlist
> Delete playlist

## Commands for manage selected playlists:
### public-playlist add :name_or_url
> Add music selected playlist
### public-playlist update :playlist :id :name_or_url
> Update music selected playlist
### public-playlist delete :playlist :id
> Delete music selected playlist
### public-playlist show :playlist
> Show all music selected playlist
### public-playlist show_all
> Show all playlist with created users
