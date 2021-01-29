import fileinput, sys

def replace_yaml(change_cause,image_name):
    # Read in the file
    with open('ingress-deployment.yaml', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('{change-cause}', change_cause)
    filedata = filedata.replace('{image-name-version}', image_name)

    # Write the file out again
    with open('ingress-deployment.yaml', 'w') as file:
        file.write(filedata)

if __name__ == "__main__":
    n = len(sys.argv)
    print("Total arguments passed:", n)
    if (n != 3):
        print ("Input parameters are incorrect!!!")
    else:
        replace_yaml(sys.argv[1],sys.argv[2])
