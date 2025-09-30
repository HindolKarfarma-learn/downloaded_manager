# every extention and their destination directory is stored here
# User may add their own extention and their destination relation
def destinationPath(ext: str) -> str:  # type hinting for faster readability
    match ext:
        case ".png":
            path = "~/Pictures/Managed/"

        case ".jpg":
            path = "~/Pictures/Managed/"

        case ".jpeg":
            path = "~/Pictures/Managed/"

        case ".svg":
            path = "~/Pictures/Managed/"

        case ".webp":
            path = "~/Pictures/Managed/"

        case ".mp4":
            path = "~/Videos/Managed/"

        case ".pdf":
            path = "~/Documents/Managed/"

        case ".tar":
            path = "~/Documents/Managed/"

        case ".gz":
            path = "~/Documents/Managed/"

        case ".zip":
            path = "~/Documents/Managed/"

        case ".docx":
            path = "~/Documents/Managed/"

        case ".docs":
            path = "~/Documents/Managed/"

        case ".odf":
            path = "~/Documents/Managed/"

        case _:
            path = "~/Downloads/"

    return path

def extractExtention(fileName: str)->str:
    dotPos=0    # full name if "." not present
    for i in range (len(fileName)-1,-1,-1) : # remember ranges stops at one element before
        if fileName[i] == ".":
            dotPos=i
            break
        else:
            continue

    return (fileName[dotPos:])
