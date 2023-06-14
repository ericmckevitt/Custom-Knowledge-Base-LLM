# Custom Knowledge-base LLM
## Eric McKevitt

## About:  

In this project, I use the LangChain library along with the OpenAI gpt-3.5-turbo model in order to train a LLM on a custom dataset. A vector store is created using the aggregated texts in order to perform similarity search on the data given some query. A map_reduce chain is used to provide an answer to the query and provide sources. The choice of map_reduce as the chain is due to the large size of expected inputs. In addition to an answer for the query, the chain also returns all intermediate steps taken to arrive at the answer as well as document sources for the answer.

--- 

## How To Run: 

- Make sure you have installed all the packages in `requirements.txt` using pip. 
- Configure your `OPENAI_API_KEY` environment variable. 
- Set a path to a parent folder, which may contain subfolders, of markdown files. 
- Set a value for the `query` variable. This is the question you want to model to respond to. 
- Run `main.py`. For large inputs with 1,000+ files, this may take a minute. Inputs < 100 files will take a matter of seconds. 

---

## Example Execution: 

In this example, I ask the LLM to find out what I have worked on at Ford Credit Organization thus far in my internship. The corpus of documents provided is the collection of all my markdown notes from the Obsidian note-taking app. Answers to this question will be scattered around different documents. This is a nuanced query, in that the model will need to differentiate between work done for Ford Credit Organization and Ford Motor Company. 

**Input Query:** <em>"What have I worked on at Ford Credit Organization so far? Do not conflate this with my work at Ford Motor Company."</em>

**Output:** <em>"I have worked on modernizing the Dealer Information System website using Angular for mobile responsiveness, adding new forms with validation and http request capabilities to the Dealer Information System, and modernizing PrimeNG tables by writing media queries to increase their mobile responsiveness.    

Sources:
* Extended Resume.md
* Ford Credit Organization.md"
</em>

> **Note:** The sentences the model came up with are entirely new sentences that appear nowhere in my corpus of notes in that exact language, but all of the information reported is correct and is aggregated from several sources. 
