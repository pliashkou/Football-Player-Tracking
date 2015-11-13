import cv2
import cv2.cv as cv

# Hue profiles based on first frame of videos

white_keeper_hp = 74
green_keeper_hp = 73
red_player_hp = 40
blue_player_hp = 76
referee_hp = 50
linesman_hp = 25

# Range width

range_width = 10
range_width_half = range_width / 2

def is_white_keeper(average_hue):
    if average_hue in range(white_keeper_hp - range_width_half, white_keeper_hp + range_width_half):
        return True
    return False

def is_green_keeper(average_hue):
    if average_hue in range(green_keeper_hp - range_width_half, green_keeper_hp + range_width_half):
        return True
    return False

def is_red_player(average_hue):
    if average_hue in range(red_player_hp - range_width_half, red_player_hp + range_width_half):
        return True
    return False

def is_blue_player(average_hue):
    if average_hue in range(blue_player_hp - range_width_half, blue_player_hp + range_width_half):
        return True
    return False

def is_referee(average_hue):
    if average_hue in range(referee_hp - range_width_half, referee_hp + range_width_half):
        return True
    return False

def is_linesman(average_hue):
    if average_hue in range(linesman_hp - range_width_half, linesman_hp + range_width_half):
        return True
    return False

def average_hue(x, y, width, height, frame):
    sum = 0
    n_points = 0
    for i in range(x, x + width + 1):
        for j in range(y, y + height + 1):
           sum += frame[j, i, 0]
           n_points += 1
    return sum / n_points

def white_keeper(first_frame):    
    hue_avg = average_hue(x=401, y=1615, width=20, height=60, frame=first_frame)
    print ("White keeper: %d" % (hue_avg))

def green_keeper(first_frame):    
    hue_avg = average_hue(x=296, y=941, width=18, height=32, frame=first_frame)
    print ("Green keeper: %d" % (hue_avg))

def red_player(first_frame):    
    hue_avg = average_hue(x=491, y=210, width=46, height=74, frame=first_frame)
    print ("Red player: %d" % (hue_avg))

def blue_player(first_frame):    
    hue_avg = average_hue(x=270, y=377, width=14, height=45, frame=first_frame)
    print ("Blue player: %d" % (hue_avg))

def referee(first_frame):    
    hue_avg = average_hue(x=309, y=197, width=20, height=50, frame=first_frame)
    print ("Referee: %d" % (hue_avg))

def linesman(first_frame):    
    hue_avg = average_hue(x=589, y=1562, width=23, height=70, frame=first_frame)
    print ("Linesman: %d" % (hue_avg))
    
# def hue_profile():
#     cap = cv2.VideoCapture("football_left.mp4")
#     _,f = cap.read()
#     print "Profiling hue averages of the following objects:"
#     white_keeper(f)
#     cap.release()
#     cap = cv2.VideoCapture("football_right.mp4")
#     _,f = cap.read()
#     green_keeper(f)
#     red_player(f)
#     blue_player(f)
#     referee(f)
#     linesman(f)
#     cap.release()

# def main():
#     hue_profile()

# main()
# print "Done!"
