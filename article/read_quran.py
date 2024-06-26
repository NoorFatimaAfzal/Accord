import tkinter as tk
import requests
import pygame.mixer
import os
import tempfile
import shutil

# audio ko play karny k liye 
pygame.mixer.init()

root = tk.Tk()
root.title("Quran Surahs")
current_dir = os.path.dirname(os.path.realpath(__file__))
logo_path = os.path.join(current_dir, "favicon.ico")
root.iconbitmap(logo_path)

def fetch_data():
    response = requests.get('http://api.alquran.cloud/v1/surah')
    data = response.json()
    return data['data']

quran_data = fetch_data()

def surah_selected(event):
    ayah_text.config(state=tk.NORMAL)
    selected_surah = surah_list.curselection()[0]
    surah_id = quran_data[selected_surah]['number']
    response = requests.get(f'http://api.alquran.cloud/v1/surah/{surah_id}/en.asad')
    surah_data = response.json()['data']
    ayah_text.delete('1.0', tk.END)
    if surah_id != 9:
        ayah_text.insert(tk.END, "بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\n\n", 'center')
    for ayah in surah_data['ayahs']:
        ayah_text.insert(tk.END, f"Ayah {ayah['numberInSurah']}:", 'bold')
        ayah_text.insert(tk.END, f" {ayah['text']}\n\n")
    ayah_text.config(state=tk.DISABLED)
    global audio_urls
    audio_urls = [ayah['audio'] for ayah in audio_data['surahs'][selected_surah]['ayahs']]

def play_audio():
    if pygame.mixer.music.get_busy():  # Check if the audio is playing
        pygame.mixer.music.stop()  # If it is, stop the audio
    elif audio_urls:  # If the audio is not playing, check if there are audio URLs
        audio_url = audio_urls.pop(0)
        audio_response = requests.get(audio_url, stream=True)
        if audio_response.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                audio_path = fp.name
                audio_response.raw.decode_content = True
                shutil.copyfileobj(audio_response.raw, fp)
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

def go_back():
    with open('previous_page.txt', 'r') as f:
        previous_page = f.read().strip()
    root.withdraw()
    os.system(f'python "{previous_page}"')
    root.destroy()

def open_help(page):
    with open('previous_page.txt', 'w') as f:
        f.write(page)
    root.withdraw()
    os.system('python "C:\\Users\\InfoBay\\OneDrive\\Desktop\\Accord\\help\\help.py"')
    root.destroy()


ayah_frame = tk.Frame(root)
ayah_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

pygame.mixer.init()

audio_response = requests.get('https://api.alquran.cloud/v1/quran/ar.alafasy')
audio_data = audio_response.json()['data']

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

vscrollbar = tk.Scrollbar(ayah_frame)
vscrollbar.grid(row=1, column=3, sticky='ns')

# Text widget for Ayahs
ayah_text = tk.Text(ayah_frame, wrap=tk.WORD, yscrollcommand=vscrollbar.set, font=('Arial', 16))
ayah_text.grid(row=1, column=0, columnspan=3, sticky='nsew')

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

# Initialize the Pygame video system
pygame.display.init()

# Play Audio Button
play_button = tk.Button(ayah_frame, text="Play Audio", font=("Arial", 15), bg="sky blue", fg="black",  command=play_audio)
play_button.grid(row=0, column=1, padx=20, pady=5)

# back button
back_button = tk.Button(ayah_frame, text="Back", font=("Arial", 15), bg="sky blue", fg="black", command=go_back)
back_button.grid(row=0, column=0, padx=20, pady=5)

# help button
help_button=tk.Button(ayah_frame,text="Help",font=("Arial", 15), bg="sky blue", fg="black",command=lambda: open_help("PostArticle"))
help_button.grid(row=0, column=2, padx=20, pady=5)


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == SONG_END:
            play_audio()
    root.update()