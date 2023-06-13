from langchain.document_loaders import DirectoryLoader

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI


def load_documents(parent_folder_path: str, progress_bar: bool = False):
    # Get all markdown files in parent folder and subfolders
    loader = DirectoryLoader(parent_folder_path, glob="**/*.md", show_progress=True)

    documents = loader.load()

    return documents


def main():
    parent_folder_path = "/Users/ericmckevitt/Documents/Obsidian"

    documents = load_documents(parent_folder_path, progress_bar=True)

    # Split the documents into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Convert texts from list[Document] to list[str]
    full_documents = [text.metadata for text in texts]
    texts = [text.page_content for text in texts]

    # Create a Chroma vector store from the texts
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_texts(
        texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]
    )

    # Perform a similarity search over the texts
    query = "What have I worked on at Ford Credit Organization so far? Do not conflate this with my work at Ford Motor Company."
    docs = docsearch.similarity_search(query)

    # Use the stuff chain to answer the question with sources
    chain = load_qa_with_sources_chain(
        OpenAI(temperature=0), chain_type="map_reduce", return_map_steps=True
    )
    output = chain({"input_documents": docs, "question": query}, return_only_outputs=True)

    print(output['output_text'])


if __name__ == "__main__":
    main()
