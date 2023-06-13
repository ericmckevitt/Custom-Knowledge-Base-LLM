# Custom Knowledge-base LLM
## Eric McKevitt

How To Run: 

- Make sure you have installed all the packages in `requirements.txt` using pip. 
- Configure your `OPENAI_API_KEY` environment variable. 
- Set a path to a parent folder, which may contain subfolders, of markdown files. 
- Set a value for the `query` variable. This is the question you want to model to respond to. 
- Run `main.py`. For large inputs with 1,000+ files, this may take a minute. Inputs < 100 files will take a matter of seconds. 