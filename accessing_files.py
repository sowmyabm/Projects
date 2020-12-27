from src.constants import DATA_FILES_PATH
from src.constants import CLIENT_FILES_PATH
from src.constants import PROPERTIES_YAML
from src.data_files.property_filr_reader import property

file_path = DATA_FILES_PATH
client_path = CLIENT_FILES_PATH


def file_details(file_d, client_p):
    print("inside file details")
    if file_d != "":
        print("file path=====>>", file_d)
    else:
        print("file does not exist")
    print("client_file_path", client_p)
    return file_d, client_p


def data_detials(f, c):
    print("inside data_details")
    print("file_path-", f)
    print("clien_path", c)
    get_file_data = file_details(f, c)
    print(get_file_data)


def main():
    YAML_DATA= property(PROPERTIES_YAML)
    print("inside main")
    file_details(file_path, client_path)
    data_detials(file_path, client_path)
    print(YAML_DATA)


if __name__ == '__main__':
    main()
