import csv
import os

def read_score(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        score = line.split(': ')[-1]  # Extract the score part after the colon
        return float(score)

def read_essay(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def convert_to_csv():
    output_file_path = 'essays_scores.csv'
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header row
        csvwriter.writerow(['essay', 'score'])
        
        for i in range(103):
            score_file_path = f'essays_all/score{i:03d}.txt'
            essay_file_path = f'essays_all/essay{i:03d}.txt'
            
            if os.path.exists(score_file_path) and os.path.exists(essay_file_path):
                score = read_score(score_file_path)
                essay = read_essay(essay_file_path)
                
                # Write the essay and score in the same row
                csvwriter.writerow([essay, score])

# Call the function to convert to CSV
convert_to_csv()
