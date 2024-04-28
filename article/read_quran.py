import tkinter as tk
import requests
import pygame.mixer

# Initialize the mixer module
pygame.mixer.init()

root = tk.Tk()
root.title("Quran Surahs")

# Function to fetch Surah data from API
def fetch_data():
    response = requests.get('http://api.alquran.cloud/v1/surah')
    data = response.json()
    return data['data']

# Fetch Surah data from API
quran_data = fetch_data()



# Function to handle Surah selection
def surah_selected(event):
    # Enable the Text widget
    ayah_text.config(state=tk.NORMAL)
    selected_surah = surah_list.curselection()[0]
    surah_id = quran_data[selected_surah]['number']
    response = requests.get(f'http://api.alquran.cloud/v1/surah/{surah_id}/en.asad')
    surah_data = response.json()['data']
    # Clear the Text widget
    ayah_text.delete('1.0', tk.END)
    # Insert "Bismillah" before each Surah except Surah At-Tawbah
    if surah_id != 9:
        ayah_text.insert(tk.END, "بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\n\n", 'center')
    # Insert each Ayah into the Text widget
    for ayah in surah_data['ayahs']:
        ayah_text.insert(tk.END, f"Ayah {ayah['numberInSurah']}:", 'bold')
        ayah_text.insert(tk.END, f" {ayah['text']}\n\n")
    # Disable the Text widget
    ayah_text.config(state=tk.DISABLED)
    global audio_urls
    audio_urls = [ayah['audio'] for ayah in audio_data['surahs'][selected_surah]['ayahs']]


# Frame for Ayah labels and Scrollbars
ayah_frame = tk.Frame(root)
ayah_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


import tempfile
import shutil

# Initialize the mixer module
pygame.mixer.init()

# Fetch the audio data from the API
audio_response = requests.get('https://api.alquran.cloud/v1/quran/ar.alafasy')
audio_data = audio_response.json()['data']


# Function to play audio
def play_audio():
    if pygame.mixer.music.get_busy():
        return
    if audio_urls:
        # Download the first audio file to a temporary file
        audio_url = audio_urls.pop(0)
        audio_response = requests.get(audio_url, stream=True)
        if audio_response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                audio_path = fp.name
                audio_response.raw.decode_content = True
                shutil.copyfileobj(audio_response.raw, fp)
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

# Play Audio Button
play_button = tk.Button(ayah_frame, text="Play Audio", command=play_audio)
play_button.pack()


# Vertical Scrollbar
vscrollbar = tk.Scrollbar(ayah_frame)
vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text widget for Ayahs
ayah_text = tk.Text(ayah_frame, wrap=tk.WORD, yscrollcommand=vscrollbar.set, font=('Arial', 16))
ayah_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure Scrollbar to command Text widget view
vscrollbar.config(command=ayah_text.yview)

# Configure a tag for centered text
ayah_text.tag_configure('center', justify='center')

# Configure a tag for bold text
ayah_text.tag_configure('bold', font=('Arial', 16, 'bold'))

# Listbox for Surah names
surah_list = tk.Listbox(root, selectmode=tk.SINGLE, width=20, font=('Arial', 16))
for surah in quran_data:
    surah_list.insert(tk.END, f"{surah['number']}. {surah['englishName']}")
surah_list.pack(side=tk.LEFT, fill=tk.Y, expand=False)

# Bind Surah selection event
surah_list.bind("<<ListboxSelect>>", surah_selected)


root.mainloop()