from langchain.document_loaders import DirectoryLoader

def main():
    parent_folder_path = '/Users/ericmckevitt/Documents/Obsidian'

    # Get all markdown files in parent folder and subfolders
    loader = DirectoryLoader(parent_folder_path, glob='**/*.md', show_progress=True)

    documents = loader.load()

    for document in documents[:1]:
        # print(document)
        print(document)
        print(type(document))
        print(document.__dir__)

if __name__ == '__main__':
    main()