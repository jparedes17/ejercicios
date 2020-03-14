def recite(start_verse, end_verse):
    list_of_gifts = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."
    ]

    day_dict = {1: 'first',     \
                2: 'second',    \
                3: 'third',     \
                4: 'fourth',    \
                5: 'fifth',     \
                6: 'sixth',     \
                7: 'seventh',   \
                8: 'eighth',    \
                9: 'ninth',     \
                10: 'tenth',    \
                11: 'eleventh', \
                12: 'twelfth'}

    result = []
    for i in range(start_verse, end_verse+1):
        verse = ''
        verse += "On the " + day_dict[i] + " day of Christmas my true love gave to me: "
        for gift in list_of_gifts[12-i:11]: 
            verse += gift
        verse += "a Partridge in a Pear Tree." if i == 1 else list_of_gifts[11]
        result.append(verse)

    return result
