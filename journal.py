import os  # Import the os module for interacting with the operating system
import json  # Import the json module for working with JSON data
from datetime import datetime  # Import the datetime module for handling dates and times

# Define the directory where data will be stored
data_dir = 'data'
# Define the file path for storing journal entries
entries_file = os.path.join(data_dir, 'entries.json')

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Function to load journal entries from the JSON file
def load_entries():
    if os.path.exists(entries_file):  # Check if the entries file exists
        with open(entries_file, 'r') as file:  # Open the file in read mode
            return json.load(file)  # Load and return the JSON data
    return []  # Return an empty list if the file doesn't exist

# Function to save journal entries to the JSON file
def save_entries(entries):
    with open(entries_file, 'w') as file:  # Open the file in write mode
        json.dump(entries, file, indent=4)  # Dump the entries as JSON with indentation

# Function to analyze the emotion of a given text
def analyze_emotion(text):
    # Define a dictionary of emotions and their associated keywords
    emotions = {
        'happy': ['happy', 'joyful', 'excited'],
        'sad': ['sad', 'depressed', 'unhappy'],
        'angry': ['angry', 'mad', 'furious'],
        'neutral': ['okay', 'fine', 'neutral']
    }
    # Initialize a dictionary to count the occurrences of each emotion
    emotion_score = {'happy': 0, 'sad': 0, 'angry': 0, 'neutral': 0}
    words = text.lower().split()  # Split the text into words and convert to lowercase
    for word in words:  # Iterate over each word
        for emotion, keywords in emotions.items():  # Iterate over each emotion and its keywords
            if word in keywords:  # Check if the word is a keyword for the emotion
                emotion_score[emotion] += 1  # Increment the emotion score
    # Return the emotion with the highest score
    return max(emotion_score, key=emotion_score.get)

# Function to remove a journal entry
def remove_entry(entries):
    print("\nRemove Entry:")
    for i, entry in enumerate(entries):  # List all entries with their index
        print(f"{i + 1}. {entry['date']}: {entry['emotion']}")
    index = int(input("Enter the number of the entry to remove: ")) - 1  # Get the entry number to remove
    if 0 <= index < len(entries):  # Check if the index is valid
        removed_entry = entries.pop(index)  # Remove the entry from the list
        save_entries(entries)  # Save the updated entries
        print(f"Removed entry from {removed_entry['date']}")  # Confirm removal
    else:
        print("Invalid entry number.")  # Print error message for invalid index

# Function to edit a journal entry
def edit_entry(entries):
    print("\nEdit Entry:")
    for i, entry in enumerate(entries):  # List all entries with their index
        print(f"{i + 1}. {entry['date']}: {entry['emotion']}")
    index = int(input("Enter the number of the entry to edit: ")) - 1  # Get the entry number to edit
    if 0 <= index < len(entries):  # Check if the index is valid
        new_entry = input("Write your new journal entry: ")  # Get the new entry text
        new_emotion = analyze_emotion(new_entry)  # Analyze the emotion of the new entry
        entries[index]['entry'] = new_entry  # Update the entry text
        entries[index]['emotion'] = new_emotion  # Update the emotion
        save_entries(entries)  # Save the updated entries
        print(f"Edited entry from {entries[index]['date']} with new emotion: {new_emotion}")  # Confirm edit
    else:
        print("Invalid entry number.")  # Print error message for invalid index

# Main function to run the journal application
def main():
    entries = load_entries()  # Load existing entries
    print("Welcome to your personal journal!")
    while True:
        # Display the main menu
        print("\n1. Write a new entry")
        print("2. View mood trend")
        print("3. Remove an entry")
        print("4. Edit an entry")
        print("5. Exit")
        choice = input("Choose an option: ")  # Get the user's choice
        if choice == '1':
            entry = input("Write your journal entry: ")  # Get the new journal entry
            emotion = analyze_emotion(entry)  # Analyze the emotion of the entry
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current date and time
            entries.append({'date': date, 'entry': entry, 'emotion': emotion})  # Add the entry to the list
            save_entries(entries)  # Save the updated entries
            print(f"Entry saved with detected emotion: {emotion}")  # Confirm save
        elif choice == '2':
            print("\nMood Trend:")
            for entry in entries:  # List all entries with their date and emotion
                print(f"{entry['date']}: {entry['emotion']}")
        elif choice == '3':
            remove_entry(entries)  # Call the function to remove an entry
        elif choice == '4':
            edit_entry(entries)  # Call the function to edit an entry
        elif choice == '5':
            break  # Exit the application
        else:
            print("Invalid choice. Please try again.")  # Print error message for invalid choice

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

