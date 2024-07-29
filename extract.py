import os
import math

def extract_evidence(file_path):
    total_score = 0
    evidence_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            if 'Evidence' in line:
                parts = line.strip().split()
                if len(parts) == 4:
                    try:
                        score = int(parts[3])
                        total_score += score
                        evidence_count += 1
                    except ValueError:
                        # Skip rows where the score is not an integer
                        continue
    
    if evidence_count == 0:
        return 0

    mean_score = total_score / evidence_count
    return (mean_score / 5)*10

def extract_persuasiveness(file_path):
    total_score = 0
    persuasiveness_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            if 'Persuasiveness' in line:
                parts = line.strip().split()
                if len(parts) == 4:
                    try:
                        score = int(parts[3])
                        total_score += score
                        persuasiveness_count += 1
                    except ValueError:
                        # Skip rows where the score is not an integer
                        continue
    
    if persuasiveness_count == 0:
        return 0

    mean_score = total_score / persuasiveness_count
    return (mean_score / 6)*10

def calculate_and_write_scores():
    for i in range(1, 103):
        output_file_path = f'essays_all/score{i:03d}.txt'
        with open(output_file_path, 'w') as output_file:
            file_path = f'essays_all/essay{i:03d}.ann'
            if os.path.exists(file_path):
                mean_persuasiveness = extract_persuasiveness(file_path)
                mean_evidence = extract_evidence(file_path)
                average_score = (mean_persuasiveness + mean_evidence) / 2
                average_score = min (10, math.floor((average_score*10+0.2)/7))

                output_file.write(f'{file_path}: {average_score:.2f}\n')

# Call the function to calculate and write the scores
calculate_and_write_scores()


# # Example usage

# file_path = 'essays_all/essay001.ann'
# mean_persuasiveness = extract_persuasiveness(file_path)
# # Example usage
# file_path = 'essays_all/essay001.ann'
# mean_evidence = extract_evidence(file_path)


# print (mean_persuasiveness)