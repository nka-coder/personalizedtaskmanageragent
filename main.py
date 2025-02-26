from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from llama_index.core import GPTVectorStoreIndex, Document
from datetime import datetime

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Task storage (in-memory for simplicity)
tasks = []

# Initialize LangChain LLM
llm = OpenAI(temperature=0.7)

# Initialize LlamaIndex with an empty document
documents = [Document(text="Task Manager Agent")]
index = GPTVectorStoreIndex(documents)

# LangChain prompt templates
add_task_template = PromptTemplate(
    input_variables=["user_input"],
    template="Extract the task description and due date (if any) from this: {user_input}"
)

recommend_template = PromptTemplate(
    input_variables=["user_input"],
    template="Provide a recommendation or tip for productivity based on this: {user_input}"
)

# LangChain chains
add_task_chain = LLMChain(llm=llm, prompt=add_task_template)
recommend_chain = LLMChain(llm=llm, prompt=recommend_template)

def add_task(task_description, due_date=None):
    """
    Adds a task to the task list with an optional due date.
    """
    task = {
        "description": task_description,
        "due_date": due_date,
        "created_at": datetime.now()
    }
    tasks.append(task)
    return f"Task added: {task_description} (Due: {due_date})"

def list_tasks():
    """
    Lists all tasks with their details.
    """
    if not tasks:
        return "No tasks found."
    task_list = "\n".join([
        f"{i+1}. {task['description']} (Due: {task['due_date']}, Created: {task['created_at']})"
        for i, task in enumerate(tasks)
    ])
    return task_list

def handle_user_input(user_input):
    """
    Processes user input and delegates to the appropriate function.
    """
    if "add task" in user_input.lower():
        # Use LangChain to extract task details
        llm_response = add_task_chain.run(user_input)
        return add_task(llm_response)
    elif "list tasks" in user_input.lower():
        return list_tasks()
    elif "recommend" in user_input.lower():
        # Use LangChain to generate a recommendation
        return recommend_chain.run(user_input)
    else:
        # Use LlamaIndex to query the task manager knowledge base
        query_engine = index.as_query_engine()
        response = query_engine.query(user_input)
        return response.response

# Example usage
if __name__ == "__main__":
    print("I'm a Personalized Task Manager Agent!")
    while True:
        user_input = input("\nWhat would you like to do? (e.g., 'Add task: Buy groceries by tomorrow', 'List tasks', 'Recommend a productivity tip'): ")
        response = handle_user_input(user_input)
        print(response)