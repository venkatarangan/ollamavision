# ollama pull llama3.2-vision
# pip install ollama

import ollama
import sys
import os
import time

def analyze_image(image_path, output_file=None):
    if not os.path.isfile(os.path.abspath(image_path)):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': (
                'What is in this image?. If you find text, please read the entire text '
                'carefully for me, neatly formatted, Don\'t miss out any words, ' 
                'Don\'t hallucinate, or rely on your memory about the subject in the text.' 
                'And please stay grounded to the facts in the image.'
            ),
            'images': [image_path]
        }]
    )

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as file:
            try:
                content = response['message']['content']
                if content:
                    print(content)
                    file.write(content)
                else:
                    file.write("Error: No content in the response.")
            except (IndexError, AttributeError) as e:
                file.write(f"Error: Failed to retrieve content. Exception: {e}")
        print(f"Response written to '{output_file}'")
    else:
        print(response)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python readimage.py <image_path> [output_file]")
    else:
        image_path = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) == 3 else None
        
        start_time = time.time()
        
        analyze_image(image_path, output_file)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print(f"Execution time: {formatted_time}")
