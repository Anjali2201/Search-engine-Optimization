# Search Engine Implementation using Python

This guide will walk you through the process of setting up the search engine and using a virtual environment using `venv`.

## Prerequisites

- Python is installed on your Windows machine. If not, download and install the latest version of Python from the official website: [Python Downloads](https://www.python.org/downloads/)

## Step 1: Clone the Repository

1. Open a Command Prompt (CMD) or PowerShell window.
2. Navigate to the directory where you want to clone the repository:
   ```
   cd path\to\your\desired\folder
   ```
3. Clone the repository using the following command:
   ```
   git clone https://github.com/username/repository.git
   ```

## Step 2: Create a Virtual Environment

1. After cloning the repository, navigate to the project directory:
   ```
   cd repository
   ```
2. Create a new virtual environment named "venv" using the following command:
   ```
   python -m venv venv
   ```

## Step 3: Activate the Virtual Environment

1. To activate the virtual environment, navigate to your project directory in the Command Prompt or PowerShell.
2. Activate the virtual environment by running:

   - Command Prompt:
     ```
     venv\Scripts\activate
     ```
   - PowerShell:
     ```
     .\venv\Scripts\Activate.ps1
     ```

   Once activated, you'll notice that the prompt changes to show the name of your virtual environment, indicating that you're now working within it.

## Step 4: Install Libraries

1. With the virtual environment active, you can install Python libraries using `pip`, just like you would in a global Python installation.
   ```
   pip install requests beautifulsoup4 nltk
   ```

## Step 5: Deactivate the Virtual Environment

1. To exit the virtual environment and return to the global Python environment, simply run the following command:
   ```
   deactivate
   ```

## Using the Virtual Environment

- Whenever you want to work on your project, remember to activate the virtual environment first.
- Install all project-specific dependencies within the virtual environment to keep your project isolated from other Python installations.
