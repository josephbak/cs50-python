def main():
    image_types = ["gif", "jpg", "jpeg", "png"]
    application_types = ["pdf", "zip"]

    file_name = input("File name: ").lower().strip()
    file_ext = file_name.split(".")[-1] 

    if file_ext in image_types:
        if file_ext in ["jpg", "jpeg"]:
            print("image/jpeg")
        else:
            print("image/", file_ext, sep="")

    elif file_ext in application_types:
        print("application/", file_ext, sep="")
    elif file_ext == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()