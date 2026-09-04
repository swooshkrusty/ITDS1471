# use csv module to read and write csv file

import csv

def main():
    """ the main function as entry point"""
    file_name = input ("Enter the filename: ")
    data = read_from_csv(file_name)
    dict_frequency = generate_frequency_list(data)
    write_frequency_to_csv(dict_frequency)

def read_from_csv(filename):
    """Read data from a CSV file."""
    # with open(filename, "r") as infile:
    #     reader = csv.reader(infile)
    #     for row in reader:
    #         print(row)
    try:
        with open(filename, "r", newline='', encoding='utf-8') as infile:
            data = csv.reader(infile)
            rows = list(data)
            print(rows)
        return rows

    except FileNotFoundError:
        print(f"{filename} does not exist")
        return None
    except Exception as ex:
        print(ex)
        return None
def generate_frequency_list(data):
    """generate a frequency list from the data"""
    co_dict = {}
    for row in data [1:]:
        co = row[1]
        if co in co_dict:
            co_dict[co] += 1
        elif co == '':
            continue
        else:
            co_dict[co] = 1
    return co_dict
def write_frequency_to_csv(d):
    """ write frequency data to a CSV file """
    try:
        with open("frequency.csv", "w", newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=d.keys())
            writer.writeheader()
            writer.writerow(d)

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()