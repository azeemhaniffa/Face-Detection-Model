import os
import csv

main_dir = "C:\\Users\\ACER\\Desktop\\WISE_AI_ASSIGNMENT_MOHAMED AZEEM BIN MOHAMED HANIFFA"
annotations = []

for category in ["Genuine", "Spoof"]:
    category_dir = os.path.join(main_dir, "PART1_FACE_DATA", category)
    for gender in ["FEMALE", "MALE"]:
        gender_dir = os.path.join(category_dir, gender)
        for filename in os.listdir(gender_dir):
            if filename.endswith(".jpg"):
                annotations.append((filename, category, gender))

csv_file = "P1_FACE_DATA_FINAL.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Name", "Label", "Gender"])
    writer.writerows(annotations)
