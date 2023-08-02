import cv2
import pandas as pd
import pickle



def persist_data(data, filename):
    # Use Python built-in functions to write 'data' to 'filename'
    contents = open("filename", "w")
    contents.write(data)
    contents.close()

def read_file(filename):
    # Use Python built-in functions to read contents of 'filename' and print them to screen
    contents = open("filename", "r")
    print(contents.read())
    contents.close()

def write_file(filename, data):
    contents = open("filename", "w")
    contents.write(data)
    contents.close()
    
def delete_file(filename):
    contents = open("filename", "w")
    contents.write(data)
    contents.close()

def overwrite_file(filename, data):
    contents = open("filename", "w")
    contents.write(data)
    contents.close()
    
def append_file(filename, data):
    contents = open("filename", "a")
    contents.write(data)
    contents.close()
    
def write_binary_file(filename, data):
    contents=open(filename, 'wb')
    contents.write(data)
    contents.close()
    
        
def read_image_file(filename):
    image = cv2.imread(filename)
    return image

def read_csv_file(filename):
    contents = pd.read_csv(filename)
    return contents

def write_csv_file(filename, df):
    df.to_csv(filename)

def read_json_file(filename):
    f = open ('data.json', "r")
    contents = json.loads(f.read())

def write_json_file(filename, data):
    with open(filename, 'w') as contents:
        json.dump(data, contents)


def write_pickle_file(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def read_pickle_file(filename):
    with open(filename,'rb') as filename:
        contents=pickle.load(filename)
