    try:
            os.rename(file, new_name)
        except:
            print(f"Duplicate file found -> {file}\nDeleting File now")
            os.remove(file)
            print("\n-----------------\nFile Deleted\n")
            count += 1
            continue
    return count