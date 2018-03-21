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
	"org.openqa.selenium",
	"javafx"
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
							public_and_nonvoid_notiny_method = False
							public_attr = False

							for method in class_declr.methods:
								if public_and_nonvoid_notiny_method == False and len(method.modifiers) > 0 and \
									("public" in method.modifiers) and str(method.return_type) != "None" and \
									(str(method.body) != "None") and len(method.body) > 1:
									stat = method.body[0]
									if str(stat) != "ReturnStatement":
										public_and_nonvoid_notiny_method = True

							if public_attr == False and len(class_declr.fields) > 0:
								for field in class_declr.fields:
									if "public" in field.modifiers:
										public_attr = True

							if public_and_nonvoid_notiny_method or public_attr:
								break

						if public_and_nonvoid_notiny_method or public_attr:
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
