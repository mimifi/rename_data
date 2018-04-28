import os


def rename_files():
    path_list = os.getcwd()
    os.chdir(path_list + "/around_the_world")
    data_list = os.listdir(os.getcwd())

    print data_list

    for data in data_list:
        print ("Old name: " + data)
        print ("New name: " + data.translate(None, "0123456789"))
        os.rename(data, data.translate(None, '0123456789'))


rename_files()
