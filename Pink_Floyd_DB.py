# Pink Floyd DB
from time import sleep

Text = open("Pink_Floyd_DB.TXT", "r")
count = 0


def discographyGenerator(f):  # Generate discography dictionaries from "Pink_Floyd_DB.TXT"
    discography, songTime = dict(), dict()
    album, song, lyrics, long, flag = '', '', '', '', 0

    for x in f:
        # album
        if x[0] == '#':
            if lyrics != '':
                discography[album][song] = lyrics
                song, album = '', ''
            lyrics = ''
            for c in x[1:-1]:
                if c == ':':
                    flag += 1
                elif flag == 2:
                    continue
                else:
                    album += c.lower()
            discography[album] = dict()
            flag = 0

        # songs
        elif x[0] == '*':
            if lyrics != '':
                discography[album][song] = lyrics
                song = ''
            lyrics = ''
            for c in x[1:-1]:
                if c == ':':
                    flag += 1
                elif flag == 0:
                    song += c.lower()
                elif flag == 4 or flag == 5:
                    long += c
                elif flag == 7:
                    lyrics += c.lower()
            lyrics += ' '
            long = long[:2] + ':' + long[2:]
            songTime[song] = long
            discography[album][song] = None
            long = ''
            flag = 0

        # lyrics
        else:
            for c in x[:-1]:
                lyrics += c.lower()
            lyrics += ' '

    # in case of the final lyrics
    if lyrics != '':
        discography[album][song] = lyrics

    return discography, songTime


def operations(dis, time, cnt):  # Operation control for the user
    # for accessing second level keys in "dis" dictionary
    tempDis = dict()
    for key in dis.values():
        tempDis.update(key)

    # user-friendly playability
    if cnt == 0:
        user = input('Hello fellow fun of "Pink Floyd", please choose the operation to proceed(8 to exit): ')
    else:
        user = input('Welcome again, please choose the operation to proceed(8 to exit): ')

    # Prints all the album names
    if user == '1':
        print('Here are all the album names: ')
        for key in dis.keys():
            print('# ' + key)

    # A user taps the name of an album and gets a list of all the songs on this album
    elif user == '2':
        user = input('Please enter here name of an album: ')
        while user not in dis.keys():
            user = input('\"' + user + '\" is not an album name, please try again: ')
        for key in dis[user].keys():
            print('* ' + key)

    # The user taps a song name and gets its length
    elif user == '3':
        user = input('Please enter here name of a song: ')
        while user.lower() not in time.keys():
            user = input('\"' + user + '\" is not an song name, please try again: ')
        print('The length of \"' + user + '\" is: ' + time[user.lower()])

    # The user taps a song name and gets all the lyrics
    elif user == '4':
        user = input('Please enter here name of a song: ')
        while user.lower() not in tempDis.keys():
            user = input('\"' + user + '\" is not an song name, please try again: ')
        print(tempDis[user.lower()])

    # The user taps a song name and gets its album
    elif user == '5':
        user = input('Please enter here name of a song: ')
        while user.lower() not in tempDis.keys():
            user = input('\"' + user + '\" is not an song name, please try again: ')
        for key, value in dis.items():
            if user.lower() in value.keys():
                print('The album name of \"' + user + '\" song is: ' + key)

    # The user types in a word and gets the names of all the songs that include the word
    elif user == '6':
        flag1 = 0
        user = input('Please enter here string of a song: ')
        for key, value in tempDis.items():
            if user.lower() in key:
                print(key)
                flag1 += 1
        if flag1 == 0:
            print('There is not \"' + user + '\" word in any of song titles')

    # The user types in a word and gets the names of all the songs that include the word
    elif user == '7':
        flag2 = 0
        user = input('Please enter here string of a song: ')
        for key, value in tempDis.items():
            if user.lower() in value:
                print(key)
                flag2 += 1
        if flag2 == 0:
            print('There is not \"' + user + '\" word in any of song lyrics')

    elif user == '8':
        print('Thank you kind stranger for viewing my code :)')
        print('Have a nice day!')
        sleep(5)
        return

    else:
        print('Wrong input, try again')
        operations(dis, time, cnt + 1)
    operations(dis, time, cnt + 1)


discograph, songTim = discographyGenerator(Text)
operations(discograph, songTim, count)

# Made by : Dmitry Simon
