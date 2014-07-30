from general import mkcmd
from general import inttohexstr


def get_ipod_type():
    return mkcmd(4, "0012")

def get_ipod_name():
    return mkcmd(4, "0014")

def set_playlist_to_all():
    return mkcmd(4, "0016")


def switch_to_type(type = 0, number = 0):
    return mkcmd(4, "0017" + inttohexstr(type ,1) + inttohexstr(number))


def get_type_count(type = 0):
    return mkcmd(4, "0018" + inttohexstr(type, 1))

def get_type_range(type = 0, count = 0, offset = 0):
    return mkcmd(4, "001A" + inttohexstr(type, 1) + inttohexstr(offset) + inttohexstr(count))

def get_time_and_status():
    return mkcmd(4, "001C")

def get_playlist_position():
    return mkcmd(4, "001E")

def get_song_title(x = 0):
    return mkcmd(4, "0020" + inttohexstr(x))

def get_song_artist(x = 0):
    return mkcmd(4, "0022" + inttohexstr(x))

def get_song_album(x = 0):
    return mkcmd(4, "0024" + inttohexstr(x))

def set_pulling_mode(mode = 0):
    return mkcmd(4, "0026" + inttohexstr(mode, 1))

def excute_playlist_switch(song = 0xFFFFFFFF):
    return mkcmd(4, "0028" + inttohexstr(song))

def raw_control(cmd = 1):
    return mkcmd(4, "0029" + inttohexstr(cmd, 1))

def play():
    return raw_control()

def pause():
    return raw_control(2)

def skip_forward():
    return raw_control(3)

def skip_backwards():
    return raw_control(4)

def forward():
    return raw_control(5)

def backward():
    return raw_control(6)

def stop_fb():
    return raw_control(7)

def get_shuffle():
    return mkcmd(4, "002C")

def set_shuffle(mode = 0):
    return mkcmd(4, "002E" + inttohexstr(mode, 1))

def get_repeat():
    return mkcmd(4, "002F")

def set_repeat(mode = 0):
    return mkcmd(4, "0031" + inttohexstr(mode, 1))

def get_playlist_songs():
    return mkcmd(4, "0035")

def set_song_in_playlist(song = 0):
    return mkcmd(4, "0037" + inttohexstr(song))
