from fuzzywuzzy import fuzz
import time
import sys

from xml_parser import (
    parse_artists,
)
from muzooka_client import get_artist_by_name


def main(argv):

    if len(argv) < 1:
        print('Missing XML file input')
        print('test_xml_artist.py <inputfile>')
        sys.exit(2)

    start_time = time.time()

    count_artist = 0
    count_artist_match = 0
    ratio_match = 0.0

    pathXML = argv[0]

    artist_limit = 150
    if len(argv) == 2:
        artist_limit = int(argv[1])

    print('Parsing artist file {}\n'.format(pathXML))

    for artist in parse_artists(pathXML):
        resp = get_artist_by_name(artist['name'])
        count_artist += 1
        if artist['name'] == resp['name']:
            count_artist_match += 1
        ratio = fuzz.token_sort_ratio(artist['name'], resp['name'])
        ratio_match += ratio / 100
        print(u'Artist {0}: Discogs: {1}({2}) - Muzooka: {3}({4}), ratio: {5}\n'.format(
            count_artist,
            artist['name'],
            artist['id'],
            resp['name'],
            resp['facebookUsername'],
            ratio,
        ))
        if artist_limit == count_artist:
            break

    ratio_avarage = ratio_match / count_artist
    elapsed_time = time.time() - start_time

    print('Resume => \n count_artist: {0} \n count_artist_match: {1} \n ratio_avarage: {2} \n Elapsed time: {3}'.format(
        count_artist,
        count_artist_match,
        ratio_avarage,
        elapsed_time,
    ))


if __name__ == '__main__':
    main(sys.argv[1:])
