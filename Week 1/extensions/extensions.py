def get_media_type(filename):
    # Extract the file extension and convert it to lowercase
    extension = filename.strip().lower().split('.')[-1]

    # Check each file extension and return the corresponding media type
    if extension == "gif":
        return "image/gif"
    elif extension == "jpg":
        return "image/jpeg"
    elif extension == "jpeg":
        return "image/jpeg"
    elif extension == "png":
        return "image/png"
    elif extension == "pdf":
        return "application/pdf"
    elif extension == "txt":
        return "text/plain"
    elif extension == "zip":
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    filename = input("Enter the name of a file: ")
    media_type = get_media_type(filename)
    print(media_type)


main()
