import os
print(os.listdir("."))
years = 14, 15, 16, 17, 18, 19, 20, 21, 22

for y in years:
	folder = str(2000 + y)
	for file in os.listdir(folder):
		if file == file.lower(): continue
		os.system (f"git mv -f {folder}/{file} {folder}/{file.lower()}")