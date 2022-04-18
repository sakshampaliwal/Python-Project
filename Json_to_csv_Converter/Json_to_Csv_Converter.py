import json
import csv

if __name__ == '__main__':
    # Open the JSON file & load its data
    with open('test.json') as dat_file:
        json_loaded_data = json.load(dat_file)
    inside_data = json_loaded_data['gamename']

    # Opening a CSV file for writing in write mode
    with open('created_csv_file.csv', 'w') as create_csv_file:
        csv_writer = csv.writer(create_csv_file)  # we only make this variable to easily use below

        count = 0
        for cnt in inside_data:
            if count == 0:
                header = cnt.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(
                cnt.values())  # as you see here if we write above function then it will be difficult to read


