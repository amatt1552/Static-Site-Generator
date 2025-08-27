from file_manager import (
    delete_from_directory,
    copy_to_directory
    )

WORKING_DIRECTORY = "../Static-Site-Generator"

def main():
    delete_from_directory(WORKING_DIRECTORY, "public")
    copy_to_directory(WORKING_DIRECTORY, "public", "static")

if __name__ == "__main__":
    main()