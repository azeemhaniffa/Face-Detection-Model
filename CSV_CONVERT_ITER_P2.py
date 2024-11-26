import os
import csv

main_dir = "C:\\Users\\ACER\\Desktop\\WISE_AI_ASSIGNMENT_MOHAMED AZEEM BIN MOHAMED HANIFFA\\PART2_ANOMALY_DATA"
annotations = []

categories = {
    "CARPET_CONDITION": ["COLOR", "CONTAMINATION", "CUT", "GOOD", "HOLE", "THREAD"],
    "HAZELNUT_CONDITION": ["CRACK", "CUT", "GOOD", "HOLE", "PRINT"],
    "TILE_CONDITION": ["CRACK", "GLUE STRIP", "GOOD", "OIL", "ROUGH", "STROKE"]
}

for category, conditions in categories.items():
    for condition in conditions:
        condition_dir = os.path.join(main_dir, category, condition)
        if os.path.exists(condition_dir):
            for filename in os.listdir(condition_dir):
                main_label = category.split("_")[0]
                annotations.append((filename, main_label, condition))

csv_file = "P2_FINAL_DATA_ANOMALY.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Name", "Main Label", "Sub Label"])
    writer.writerows(annotations)
