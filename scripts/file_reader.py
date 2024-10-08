import db_manager.db as db

def read_file():
    file_name = input("Enter file name : " )
    data = (file_name,)
    print("reading from db...")
    image_data = db.select_file(data)

    with open("scoresheets/db_" + file_name, 'wb') as f:
        print("writing data to file...")
        f.write(image_data)


if __name__ == '__main__':
    print("\n   --->>> Starting file_reader() <<<---")
    read_file()
    print("\n--->>> FINISHED")