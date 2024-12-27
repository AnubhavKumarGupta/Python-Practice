import requests
from bs4 import BeautifulSoup

print('\n-------------------- Get the lyrics to a Song ---------------------\n')

def save_lyrics_to_text(artist, song):
    
    base_url = 'http://www.azlyrics.com/'
         
    song_url = base_url + 'lyrics/' + artist.replace(" ", "").lower() + '/' + song.replace(" ", "").lower() + '.html'

    # Use requests library to get html from artist's page
    response = requests.get(song_url)

    # Make the html soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        lyrics = soup.find('div', class_='col-xs-12 col-lg-8 text-center').find_all('div')[5].text

        # Create and write the lyrics to a text file
        filename = f'{artist}_{song}_lyrics.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Lyrics for {song} by {artist}\n\n')
            file.write(lyrics)

        print(f'Lyrics saved to {filename}')
    except AttributeError:
        print("Either this track doesn't exist or ensure the spelling is correct!")

artist = input("Enter the name of the artist/band: ")
song = input("Enter the name of the song: ")
save_lyrics_to_text(artist, song)