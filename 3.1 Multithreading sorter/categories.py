CATEGORIES = {"images": ("jpeg", "png", "jpg", "svg"),
              "video": ("avi", "mp4", "mov", "mkv"),
              "documents": ("doc", "docx", "txt", "pdf", "xlsx", "pptx", "djvu "),
              "audio": ("mp3", "ogg", "wav", "amr", "wma"),
              "archives": ("zip", "gz", "rar", "tar"),
              "other_formats": ()
              }

IGNORED_FOLDERS = tuple(CATEGORIES.keys())

ALL_EXTENSIONS = tuple(ext for ext_group in CATEGORIES.values() for ext in ext_group)
