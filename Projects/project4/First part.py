# nathan macbeth
# 2/4/26
# project 4 first part


import os


def read_user_data(file_name):
        names = []

        with open(file_name, 'r') as user_file:
            for line in user_file:
                names.append(line.strip())
        return names
        
def format_greetings(name):
            return f"Hello, {name}! Welcome!"
        
def save_greetings(file_name, greeting_list):
        with open(file_name, 'w') as file:
            for greeting in greeting_list:
                file.write(greeting + '\n')
            return True 

def main():
        input_file = "names.txt"
        output_file = "greetings.txt"

        if not os.path.exists(input_file):
            print(f"'{input_file}' not found. Creating it with default names...")
        with open(input_file, 'w') as f:
            f.write("Alice\nBob\nCharlie\n")

        raw_names = read_user_data(input_file)
                
        processed_greetings = []
        for name in raw_names:
            processed_greetings.append(format_greetings(name))

        success = save_greetings(output_file, processed_greetings)
        if success:
            print(f"Successfully processed {len(processed_greetings)} greetings!")
if __name__ == "__main__":
        main()


