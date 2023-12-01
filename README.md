# WhatsAppGPT

## Project Overview

The WhatsAppGPT Bot is an innovative solution that integrates OpenAI's powerful GPT model with WhatsApp, providing an interactive and intelligent chat experience. Designed to efficiently process and respond to user messages, this bot leverages the latest advancements in AI and natural language processing.

## Features

- **Advanced Chat Interaction**: Seamlessly processes and responds to user messages on WhatsApp in real-time.
- **Intelligent Response Generation**: Utilizes OpenAI's GPT model to generate contextually relevant and coherent responses.
- **WhatsApp Webhook Integration**: Efficiently handles incoming messages through WhatsApp webhook mechanism.
- **Automated Message Handling**: Offers automated responses to user queries, enhancing engagement.


## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configurations](#configurations)
- [API Integration](#api-integration)
- [Usage](#usage)
- [TO-DO](#to-do)

## Installation

To set up the LENA-ALPR system, follow these instructions:

1. Install Conda and create a new environment:

    ```bash
    conda create --name venv python==3.10.9
    conda activate venv
    ```

Or

2. Set Up a Virtual Environment

     ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Clone the repository:

    ```bash
    git clone https://github.com/meryemsakin/WhatsAppGPT.git
    ```

4. Navigate to the project's root directory:

    ```bash
    cd WhatsAppGPT
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

```
WHATSAPPGPT
│
├── src
│   ├── chat
│   │   └── models
│   │       └── service.py            - Chat service logic.
│   ├── databases
│   │   ├── mongo.py                  - MongoDB client setup.
│   │   └── vector.py                 - Vector database utilities.
│   ├── helpers
│   │   └── topics.py                 - Helper functions for topic management.
│   ├── huggingface_module
│   │   └── hf.py                     - HuggingFace API integration.
│   ├── models
│   │   └── __init__.py               - Pydantic models for structured data.
│   ├── openai_module
│   │   ├── prompts                   - Prompt templates for OpenAI.
│   │   ├── schemas                   - Schemas for OpenAI responses.
│   │   └── service.py                - OpenAI service integration.
│   ├── system_profile
│   │   └── models
│   │       └── __init__.py           - System profile models.
│   ├── user
│   │   └── models
│   │       └── service.py            - User management services.
│   ├── utils
│   │   └── dict.py                   - Dictionary utilities.
│   └── whatsapp_webhook
│       └── __init__.py               - WhatsApp webhook handlers.
│
├── .gitignore                        - Specifies intentionally untracked files.
├── LICENSE                           - The license for the project.
├── main.py                           - The entry point for the FastAPI application.
├── Procfile                          - Configuration for running the app on a platform.
├── README.md                         - Project description and instructions.
└── requirements.txt                  - The dependencies required for the project.
```

## Configuration

Set up the **.env** file with your API keys and tokens (refer to **config.py** for variable names).
Configure WhatsApp webhook URL in your WhatsApp API settings.

## API Integration
The bot integrates with the following APIs:

- **OpenAI GPT**: For generating chat responses.
- **WhatsApp API**: To receive and send messages on WhatsApp.
- **MongoDB**: For storing chat logs and user data.

## Usage
Start the FastAPI application using uvicorn with the following command:

```bash
uvicorn src.main:app --reload
```

The **--reload** flag enables hot reloading so the server will automatically restart upon file changes. This is useful during development.

## TO DO

- [x] Implement real-time chat interaction with WhatsApp users.
- [x] Integrate OpenAI's GPT model for intelligent response generation.
- [x] Establish a MongoDB database for message and user data storage.
- [x] Develop a scalable architecture to handle multiple simultaneous conversations.
- [ ] Enhance the chatbot's ability to understand and maintain context in conversations.
- [ ] Implement advanced analytics for tracking user engagement and chatbot performance.
- [ ] Set up a continuous integration/continuous deployment (CI/CD) pipeline.
- [ ] Conduct user testing to collect feedback for further improvements.
- [ ] Explore integration with other services and platforms to enhance bot functionality (e.g., calendar, news updates).
- [ ] Performance Optimization: Enhance response times and optimize server performance for handling high traffic.


## Contributions
Don't hesitate to share your ideas, submit pull requests, or report issues. We're excited to collaborate with you and see how your contributions will shape the future of this project. Together, we can build something truly remarkable!

If you're interested in contributing, feel free to fork the repository, make your changes, and submit a pull request. For any questions or discussions, you can open an issue.

Thank you for your interest in contributing to the WhatsAppGPT!
