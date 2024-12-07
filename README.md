# CS793-Final-Project

## Instruction

1. **Set up the environment**:

   - Ensure you are using **Python >= 3.10**. It is highly recommended to create a virtual environment for the project.
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # macOS/Linux
     .\.venv\Scripts\activate   # Windows
     ```

2. **Install required packages**:

   - Install dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure the project**:
   - Modify the `config.yaml` file with your specific settings.
   - You can refer to the [config_example.yaml](./config_example.yaml) for guidance.

## Project Structure

- **`main.py`**: Entry point for the project. [`main.py`](./main.py)
- **`agent.py`**: Core logic for handling LLM agents. [`agent.py`](./agent.py)
- **`config.yaml`**: Configuration file for LLMs and APIs.
- **`config_example.yaml`**: Example configuration file. [`config_example.yaml`](./path/to/config_example.yaml)
- **`requirements.txt`**: Dependencies required for the project. [`requirements.txt`](./requirements.txt)

## Usage

1. After setting up the environment and dependencies, run the project:
   ```bash
   python main.py
   ```
