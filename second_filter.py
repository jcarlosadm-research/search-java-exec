import javalang
import os
import shutil
import time
from shutil import copyfile

RESULTS_FOLDER = "results"
OUTPUT_FOLDER = "output"

# TODO: add more imports
INVALID_IMPORTS = {
	"javax.swing",
	"java.awt",
	"org.openqa.selenium"
}

# TODO: add more conditions
def is_invalid_line(line):
	for inv_import in INVALID_IMPORTS:
		if inv_import in line:
			return True
	return False

if not os.path.exists(OUTPUT_FOLDER):
	os.makedirs(OUTPUT_FOLDER)

dirs = next(os.walk(RESULTS_FOLDER))[1]
count = 0

for folder in dirs:
	listdirs = next(os.walk(os.path.join(RESULTS_FOLDER, folder)))[1]
	if not listdirs:
		shutil.rmtree(os.path.join(RESULTS_FOLDER, folder))
	else:
		for subfolder in listdirs:
			files = next(os.walk(os.path.join(RESULTS_FOLDER, folder, subfolder)))[2]
			if not files:
				shutil.rmtree(os.path.join(RESULTS_FOLDER, folder, subfolder))
			else:
				for file in files:
					content = ""
					invalid = False
					with open(os.path.join(RESULTS_FOLDER, folder, subfolder, file), 'r') as f:
						for line in f:
							if is_invalid_line(line):
								invalid = True
								break
							content += line

					if invalid:
						continue

					try:
						tree = javalang.parse.parse(content)

						class_declr_list = []
						for type in tree.types:
							if str(type) == "ClassDeclaration":
								class_declr_list.append(type)

						for class_declr in class_declr_list:
							for method in class_declr.methods:
								#print(dir(method))
								#print(method.position)
								#print(method.name)
								#for stat in method.body:
									#print(dir(stat))
								#	print(stat.expression.attrs)
								# print(method.body)
								if (str(method.body) != "None") and len(method.body) > 0:
									minimal_exp = False
									for stat in method.body:
										if str(stat) == "ReturnStatement":
											minimal_exp = True
										elif str(stat) == "StatementExpression" and \
										 str(stat.expression) == "Assignment":
											minimal_exp = True

									if (not minimal_exp) or (len(method.body) > 1):
										#print(method.body)
										#time.sleep(5)
										if not os.path.exists(os.path.join(OUTPUT_FOLDER,folder)):
											os.makedirs(os.path.join(OUTPUT_FOLDER,folder))
										if not os.path.exists(os.path.join(OUTPUT_FOLDER,folder,subfolder)):
											os.makedirs(os.path.join(OUTPUT_FOLDER,folder,subfolder))
										copyfile(os.path.join(RESULTS_FOLDER,folder,subfolder,file), \
											os.path.join(OUTPUT_FOLDER,folder,subfolder,file))
										count+=1
					except:
						pass
print("number of programs: " + str(count))
