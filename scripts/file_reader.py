
def read_file():
    cur.execute("SELECT image_data FROM images WHERE id = %s", (1,))
image_data = cur.fetchone()[0]

# Write the binary data to a new file
with open('retrieved_image.jpg', 'wb') as f:
    f.write(image_data)
    pass



if __name__ == '__main__':
    print("\n   --->>> Starting file_reader() <<<---")
    read_file()
    print("\n--->>> FINISHED")