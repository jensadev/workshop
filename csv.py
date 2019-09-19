# https://docs.python.org/3/howto/argparse.html
import argparse,csv
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Full file name of CSV file.", action="store_true")
args = parser.parse_args()

filehandle = ""

if args.file:
  filehandle = args.file
else:
  filehandle = input(".csv file to read: ")

# https://docs.python.org/3/tutorial/errors.html
try:
  # https://docs.python.org/3/library/csv.html
  with open(filehandle, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # id,first_name,last_name,email,gender,ip_address
      # print(row)
      username = row['first_name'][0:3] + row['last_name'][0:3] + str(19)
      print(username.lower())
except (FileNotFoundError):
  print("No such file")