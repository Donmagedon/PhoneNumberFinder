import os,re, aiofiles, itertools
result = []
numbersFound = ""
separator = "\n"
def gatherPhoneNumbers ():
 findNumber = re.compile(r"3\d{2}-?\d{3}-?\d{3,4}\s")
 curdir = os.listdir(".")

 for file in curdir:
   if(file.endswith(".txt")):
    allNumbers =  findNumber.findall(open(file).read())
    global result
    if allNumbers != []:
      result.append(allNumbers)
 result = [inner for outer in result for inner in outer]

gatherPhoneNumbers()
if result != []:
  open("output.txt","w").write("Found "+str(len(result))+" phone number/s"+"\n"+separator.join(result))
else:
  open("output.txt","w").write("Script ran successfully, NO numbers were found!")

