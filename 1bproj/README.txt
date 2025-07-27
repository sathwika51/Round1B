#  Round 1B Submission – Persona-Based PDF Content Extraction

This project is built to analyze a set of PDF files and intelligently extract content that is most relevant to a specific persona and their intended task.



##  What’s Included

The repository contains the following files and folders:

- `main.py` – The core script responsible for PDF processing  
- `Dockerfile` – Container setup for reproducible runs  
- `requirements.txt` – Python packages needed to run the script  
- `persona.json` – Describes the target user and their needs  
- `input_files/` – Place your PDF documents here (minimum of 3 files)  
- `output/result.json` – The final structured output after processing  
- `approach_explanation.md` – Summary of the methodology  
- `README.txt` – This documentation



##  Running the Project with Docker

To execute this solution in a CPU-only environment, follow these steps:

### Step 1: Build the Docker Image

Run the following command in the project directory:

```bash
docker build -t persona_extractor .
```

### Step 2: Launch the Container

Execute the container using:

```bash
docker run -v $(pwd)/input_files:/app/input -v $(pwd)/output:/app/output persona_extractor
```

Once the process completes, you’ll find the result saved under `output/result.json`.



##  Requirements

- Docker installed (either Desktop or CLI version)  
- No GPU needed — designed to run efficiently on standard CPUs  
- Total model size is below 1GB  
- Completes processing in under 60 seconds


##  Validation and Testing

This solution was locally tested with:

- Five different PDF inputs  
- A clearly defined persona and objective  
- Docker CLI on a Windows machine using WSL2



