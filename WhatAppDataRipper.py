import re
import csv
from datetime import datetime
import os
import sys
from typing import Optional, Tuple, List, Dict
import argparse
from tqdm import tqdm
from pyfiglet import Figlet
import questionary
from termcolor import colored

class DataRipper:
    """A professional CLI tool for converting WhatsApp chats to structured CSV."""
    
    def __init__(self):
        self.welcome_message()
        self.input_file, self.output_file = self.get_user_input()
        self.chat_data = []
        
    def welcome_message(self):
        """Display the welcome banner and introductory message."""
        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font='slant')
        print(colored(f.renderText('DataRipper'), 'cyan'))
        print(colored("WhatsApp Chat to CSV Converter", 'light_blue'))
        print(colored("=" * 60, 'light_grey'))
        print(colored("Transform raw WhatsApp exports into structured datasets", 'white'))
        print(colored("Perfect for analysis, machine learning, and archiving", 'white'))
        print(colored("=" * 60, 'light_grey') + "\n")
    
    def get_user_input(self) -> Tuple[str, str]:
        """Get and validate user input for input and output files."""
        while True:
            input_file = questionary.path(
                "Enter the path to your WhatsApp chat file:",
                validate=lambda path: os.path.exists(path) if path else "Please enter a valid file path"
            ).ask()
            
            if not input_file:
                sys.exit(colored("Operation cancelled by user.", 'yellow'))
            
            # Suggest output filename based on input
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            default_output = f"{base_name}_structured.csv"
            
            output_file = questionary.path(
                "Enter the output CSV file path:",
                default=default_output,
                validate=lambda path: not os.path.exists(path) or questionary.confirm(
                    "File exists. Overwrite?").ask()
            ).ask()
            
            if not output_file:
                continue  # Let user try again
                
            return input_file, output_file
    
    def parse_chat_line(self, line: str) -> Optional[Dict]:
        """Parse a single line of WhatsApp chat into structured data."""
        # Regex pattern for WhatsApp chat lines
        pattern = r'^(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}) - ([^:]+): (.+)$'
        match = re.match(pattern, line)
        
        if not match:
            return None
            
        date_str, time_str, sender, message = match.groups()
        
        # Clean sender name
        sender = sender.strip()
        
        # Parse datetime
        try:
            timestamp = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")
        except ValueError:
            try:
                timestamp = datetime.strptime(f"{date_str} {time_str}", "%m/%d/%Y %H:%M")
            except ValueError:
                timestamp = f"{date_str} {time_str}"  # Fallback to string if parsing fails
        
        # Check for media
        media_flag = bool(
            re.search(r'<Media omitted>', message) or 
            re.search(r'\.(jpg|jpeg|png|gif|mp4|mov|avi|pdf|docx?|xlsx?|pptx?|txt)$', message, re.I)
        )
        
        return {
            'timestamp': timestamp,
            'sender': sender,
            'message': message.strip(),
            'media_flag': media_flag
        }
    
    def process_file(self):
        """Process the input file and extract structured data."""
        print(colored("\nProcessing chat data...", 'light_blue'))
        
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Process with progress bar
            for line in tqdm(lines, desc="Parsing messages", unit="lines", colour='green'):
                parsed = self.parse_chat_line(line)
                if parsed:
                    self.chat_data.append(parsed)
                    
            print(colored(f"\nSuccessfully parsed {len(self.chat_data)} messages.", 'green'))
            
        except Exception as e:
            print(colored(f"\nError processing file: {str(e)}", 'red'))
            sys.exit(1)
    
    def export_to_csv(self):
        """Export the parsed data to CSV."""
        if not self.chat_data:
            print(colored("No valid messages found to export.", 'yellow'))
            return
            
        print(colored("\nExporting to CSV...", 'light_blue'))
        
        try:
            with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['timestamp', 'sender', 'message', 'media_flag']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                
                for row in tqdm(self.chat_data, desc="Writing CSV", unit="rows", colour='blue'):
                    writer.writerow(row)
                    
            print(colored(f"\nSuccessfully exported to: {self.output_file}", 'green'))
            print(colored(f"Total messages exported: {len(self.chat_data)}", 'light_grey'))
            
        except Exception as e:
            print(colored(f"\nError exporting CSV: {str(e)}", 'red'))
            sys.exit(1)
    
    def run(self):
        """Execute the full workflow."""
        self.process_file()
        self.export_to_csv()
        
        # Show completion message
        print(colored("\n" + "=" * 60, 'light_grey'))
        print(colored("DataRipper completed successfully!", 'cyan', attrs=['bold']))
        print(colored("Your WhatsApp data is now ready for analysis.", 'light_blue'))
        print(colored("=" * 60, 'light_grey'))

def main():
    try:
        tool = DataRipper()
        tool.run()
    except KeyboardInterrupt:
        print(colored("\nOperation cancelled by user.", 'yellow'))
        sys.exit(0)
    except Exception as e:
        print(colored(f"\nAn unexpected error occurred: {str(e)}", 'red'))
        sys.exit(1)

if __name__ == "__main__":
    main()