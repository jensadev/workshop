# https://docs.python.org/3/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File name to read", action="store_true")
args = parser.parse_args()

filehandle = ""

if args.file:
  filehandle = args.file
else:
  filehandle = input(".txt file to read: ")

try:
  with open(filehandle, "r") as txtfile:
    for line in txtfile:
      #print(line)
      arrline = line.split('\t') # jmf ' '
      print(arrline[1], arrline[2])
except (FileNotFoundError):
  print("No such file")