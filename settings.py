level_map = [
'                               ',
'              XXX  XX          ',
'         XXX   X   XX      XXXX',
'          X        XX          ',
'XXXXXX             XX          ',
'XXX                XXXXXX      ',
'                   XX          ',
'        XXXX       XX          ',
'    P   XXXX       XX          ',
'XXXXXXXXXXXX       XXXXXXXXXXXX']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

limit_left = screen_width * 0.20
limit_right = screen_width * 0.60

limit_up = screen_height * 0.20