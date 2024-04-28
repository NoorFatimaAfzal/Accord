import tkinter as tk
import requests

root = tk.Tk()
root.title("Quran Surahs")

# Function to fetch Surah data from API
def fetch_data():
    response = requests.get('http://api.alquran.cloud/v1/surah')
    data = response.json()
    return data['data']

# Fetch Surah data from API
quran_data = fetch_data()

# Frame for Ayah labels and Scrollbars
ayah_frame = tk.Frame(root)
ayah_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Vertical Scrollbar
vscrollbar = tk.Scrollbar(ayah_frame)
vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text widget for Ayahs
ayah_text = tk.Text(ayah_frame, wrap=tk.WORD, yscrollcommand=vscrollbar.set, font=('Arial', 16))
ayah_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure Scrollbar to command Text widget view
vscrollbar.config(command=ayah_text.yview)

# Function to handle Surah selection
def surah_selected(event):
    selected_surah = surah_list.curselection()[0]
    surah_id = quran_data[selected_surah]['number']
    response = requests.get(f'http://api.alquran.cloud/v1/surah/{surah_id}/en.asad')
    surah_data = response.json()['data']
    # Clear the Text widget
    ayah_text.delete('1.0', tk.END)
    # Insert "Bismillah" before each Surah except Surah At-Tawbah
    if surah_id != 9:
        ayah_text.insert(tk.END, "بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\n\n")
    # Insert each Ayah into the Text widget
    for ayah in surah_data['ayahs']:
        ayah_text.insert(tk.END, f"Ayah {ayah['numberInSurah']}: {ayah['text']}\n\n")
    # Disable the Text widget
    ayah_text.config(state=tk.DISABLED)

# Listbox for Surah names
surah_list = tk.Listbox(root, selectmode=tk.SINGLE, width=20, font=('Arial', 16))
for surah in quran_data:
    surah_list.insert(tk.END, f"{surah['number']}. {surah['englishName']}")
surah_list.pack(side=tk.LEFT, fill=tk.Y, expand=False)

# Bind Surah selection event
surah_list.bind("<<ListboxSelect>>", surah_selected)

root.mainloop()