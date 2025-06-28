from ursina import *

dj_tile_position = Vec3(45, 0, -45)
dj_hype_timer = 0
hype_gain_rate = 1     # how much hype to gain per tick
hype_tick_interval = 1 # every 1 second
hype_ticks_remaining = 10

# Internal counters
_time_accumulator = 0
_is_playing_track = False
hype_delta = 0

def check_dj_interaction(player):
    global _is_playing_track, _time_accumulator, hype_ticks_remaining, hype_delta

    if distance(player.position, dj_tile_position) < 1.5:
        if not _is_playing_track:
            print("DJ dropped a sick track!")
            _is_playing_track = True
            _time_accumulator = 0
            hype_ticks_remaining = 10
    else:
        _is_playing_track = False

    if _is_playing_track and hype_ticks_remaining > 0:
        _time_accumulator += time.dt
        if _time_accumulator >= hype_tick_interval:
            _time_accumulator = 0
            hype_delta += hype_gain_rate
            hype_ticks_remaining -= 1
            print("Crowd is vibing... +1 hype")

def consume_dj_effects():
    global hype_delta
    h = hype_delta
    hype_delta = 0
    return h
