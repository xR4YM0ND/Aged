import os
import json

def search_word_in_json_files(folder_path, word):
    files_with_word = []  # List to store file names with the word

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    try:
                        data = json.load(f)
                        json_str = json.dumps(data)  # Convert JSON to string for search
                        if word in json_str:
                            files_with_word.append(file_path)  # Add the file to the list
                    except json.JSONDecodeError as e:
                        print(f"Error reading {file_path}: {e}")

    return files_with_word

# Replace 'your_folder_path' with the directory path containing your JSON files
folder_path = r'C:\Users\xr4ym\OneDrive\Desktop\aged\data'
# Replace 'your_search_word' with the word you want to search for in the JSON files
search_word = 'slime_ball'

files_containing_word = search_word_in_json_files(folder_path, search_word)

if files_containing_word:
    print(f"Files containing the word '{search_word}':")
    for file in files_containing_word:
        print(file)
else:
    print(f"No files found containing the word '{search_word}'.")
