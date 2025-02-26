# Personalized Task Manager Agent

## Overview

This project is a **Personalized Task Manager Agent** that helps users manage their tasks and provides productivity recommendations. It leverages **LangChain** for natural language processing and task extraction, and **LlamaIndex** for querying a knowledge base. The agent can add tasks, list existing tasks, and provide productivity tips based on user input.

## Features

- **Add Tasks**: Users can add tasks with optional due dates. The agent uses LangChain to extract task details from natural language input.
- **List Tasks**: Users can view all tasks with their descriptions, due dates, and creation times.
- **Productivity Recommendations**: The agent can provide productivity tips or recommendations based on user input.
- **Knowledge Base Querying**: For general queries, the agent uses LlamaIndex to query a knowledge base and provide relevant responses.

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/task-manager-agent.git
   cd task-manager-agent
   ```

2. **Install Dependencies**:
Ensure you have Python 3.7+ installed. Then, install all the required packages.

3. **Set Up Environment Variables**:
Create a `.env` file in the root directory and add your OpenAI API key:

## Usage

1. **Run the Agent**:
Start the task manager agent by running:
```
python main.py
```
2. **Interact with the Agent**:
The agent will prompt you for input. You can:
    - Add a task: e.g., "Add task: Buy groceries by tomorrow"
    - List tasks: e.g., "List tasks"
    - Get a productivity recommendation: e.g., "Recommend a productivity tip"
    - Ask general questions: e.g., "How can I prioritize my tasks?"
Example interaction:
```
I'm a Personalized Task Manager Agent!

What would you like to do? (e.g., 'Add task: Buy groceries by tomorrow', 'List tasks', 'Recommend a productivity tip'): Add task: Finish the report by Friday
Task added: Finish the report (Due: Friday)

What would you like to do? List tasks
Finish the report (Due: Friday, Created: 2023-10-05 14:30:00)
```

## Code Structure

- **LangChain Integration**:
    - `LLMChain` is used to process natural language input and extract task details or generate recommendations.
    - `PromptTemplate` defines the structure of the prompts used by the LLM.

- **LlamaIndex Integration**:
`GPTVectorStoreIndex` is used to create a knowledge base for querying general information.

- **Task Management**:
    - Tasks are stored in an in-memory list, with each task having a description, due date, and creation timestamp.
    - Functions like `add_task` and `list_tasks` handle task management.

- **User Input Handling**:
    - The `handle_user_input` function processes user input and delegates to the appropriate function or chain.

## Dependencies

- **LangChain**: For natural language processing and task extraction.
- **LlamaIndex**: For querying a knowledge base.
- **OpenAI**: For accessing the GPT-3 language model.
- **dotenv**: For loading environment variables from a `.env` file.

## Future Enhancements

- **Persistent Storage**: Implement a database to store tasks persistently.
- **Task Prioritization**: Add functionality to prioritize tasks based on due dates or importance.