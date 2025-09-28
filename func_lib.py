# every extention and their destination directory is stored here
# User may add their own extention and their destination relation
def destinationPath(ext: str) -> str:  # type hinting for faster readability
    match ext:
        case ".png":
            path = "~/Pictures/Managed"

        case ".jpg":
            path = "~/Pictures/Managed"

        case ".jpeg":
            path = "~/Pictures/Managed"

        case ".svg":
            path = "~/Pictures/Managed"

        case ".webp":
            path = "~/Pictures/Managed"

        case ".mp4":
            path = "~/Videos/Managed"

        case ".pdf":
            path = "~/Documents/Managed"

        case ".tar":
            path = "~/Documents/Managed"

        case ".gz":
            path = "~/Documents/Managed"

        case ".zip":
            path = "~/Documents/Managed"

        case ".docs":
            path = "~/Documents/Managed"

        case ".odf":
            path = "~/Documents/Managed"

        case _:
            path = "~/Downloads"

    return path
