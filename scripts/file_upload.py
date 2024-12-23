import db_manager.db as db

def upload_sheet():
    week_id = input("Enter Week # : ").strip()
    file_name = "sheet" + week_id + ".jpg"

    with open("pool_files/" + file_name, 'rb') as f:
        image_data = f.read()

        print(f"\nwriting {file_name} to db...")
        data = (week_id, file_name, image_data)
        db.insert_file(data)
        print(f"finished writing {file_name}")

def upload_file():
    file_name = input("Enter file name : ")

    with open("pool_files/" + file_name, 'rb') as f:
        image_data = f.read()

        print(f"\nwriting {file_name} to db...")
        data = (0, file_name, image_data)
        db.insert_file(data)
        print(f"finished writing {file_name}")

if __name__ == '__main__':
    print("\n   --->>> Starting file_upload() <<<---")
    upload_sheet()
    #upload_file()
    print("\n--->>> FINISHED")