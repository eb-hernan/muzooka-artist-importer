import xml.etree.cElementTree as etree


def strip_tag_name(t):
    idx = t.rfind('}')
    if idx != -1:
        t = t[idx + 1:]
    return t


def calculate_level(event, tname, level, node):
    if event == 'start' and tname == node:
        return 1
    elif event == 'start':
        return level + 1
    elif event == 'end':
        return level - 1


USE_EXTRA_ARTISTS = False


def parse_artists(pathXML):
    artist = None
    level = 0

    for event, elem in etree.iterparse(pathXML, events=('start', 'end')):
        try:
            tname = strip_tag_name(elem.tag)

            level = calculate_level(event, tname, level, 'artist')

            if event == 'start' and tname == 'artist':
                artist = {
                    'id': None,
                    'biography': None,
                    'profile': None,
                    'spotify_id': None,
                    'social_media_links': [],
                }

            elif event != 'end' and level == 2:
                if tname == 'id':
                    artist['id'] = elem.text
                if tname == 'name':
                    artist['name'] = elem.text
                if tname == 'spotify_id':
                    artist['spotify_id'] = elem.text
                if tname == 'profile':
                    artist['profile'] = elem.text

            elif event != 'end' and level == 3:
                if tname == 'url':
                    artist['social_media_links'].append(elem.text)

            if event == 'end' and tname == 'artist':
                yield artist

        except etree.ParseError:
            print('>>>error parsing...continue')
        finally:
            elem.clear()
