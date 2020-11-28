if os.path.isdir(os.path.join(os.getcwd(), 'groups')):
        shutil.rmtree(os.path.join(os.getcwd(), 'groups'))
    os.mkdir('groups')