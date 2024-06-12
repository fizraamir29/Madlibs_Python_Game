import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# Function to read the story from a file
def read_story(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {filename} was not found.")
        return ""
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file: {e}")
        return ""

# Function to extract placeholders from the story
def extract_placeholders(story):
    words = set()
    start_of_word = -1
    target_start = "<"
    target_end = ">"
    
    for i, char in enumerate(story):
        if char == target_start:
            start_of_word = i
        if char == target_end and start_of_word != -1:
            word = story[start_of_word: i + 1]
            words.add(word)
            start_of_word = -1
    return words

# Function to get user inputs for placeholders
def get_user_inputs(words):
    answers = {}
    for word in words:
        answer = simpledialog.askstring("Input", f"Enter a word for {word}:")
        if answer is not None:
            answers[word] = answer
    return answers

# Function to replace placeholders with user inputs
def replace_placeholders(story, answers):
    for word, replacement in answers.items():
        story = story.replace(word, replacement)
    return story

# Function to save modified story
def save_story(filename, story):
    try:
        with open(filename, "w") as f:
            f.write(story)
        messagebox.showinfo("Success", f"Modified story saved to {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

# Main function to create and run the GUI
def main():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Read the story
    story = read_story("story.txt")
    if not story:
        return

    # Extract placeholders
    placeholders = extract_placeholders(story)
    
    # Get user inputs
    user_inputs = get_user_inputs(placeholders)
    
    # Replace placeholders with user inputs
    modified_story = replace_placeholders(story, user_inputs)
    
    # Display the modified story
    messagebox.showinfo("Modified Story", modified_story)
    
    # Save the modified story
    save_story("modified_story.txt", modified_story)
    
    # End the program
    root.destroy()

if __name__ == "__main__":
    main()
