
### Detailed Component Descriptions

#### 1. `app/main.py`
The core module housing all application logic, UI specifications, and API server configuration:
- **Ollama Client Handler (`generate_text`)**: Formulates and sends `POST` requests containing prompt strings and model identifiers (`qwen:0.5b`) to the local Ollama REST API. Includes timeout management and error handling.
- **Gradio User Interface (`gui`)**: Configures browser-based input components (multi-line prompt box, model selection dropdown) and output text containers with custom titles and descriptions.
- **FastAPI Mount (`app`)**: Instantiates the FastAPI app container and mounts the Gradio interface at the root route (`/`).
- **ASGI Server Invocation**: Uses `uvicorn.run()` to serve the application on `127.0.0.1:8000`.

#### 2. `requirements.txt`
The environment dependency manifest ensuring reproducible builds:
- `fastapi`: High-performance asynchronous web framework for Python.
- `uvicorn[standard]`: ASGI server implementation for hosting FastAPI.
- `gradio==4.28.3`: Framework for building interactive machine learning web applications.
- `requests`: HTTP client library for local API communication.
- `python-dotenv`: Environment variable configuration utility.

#### 3. `Screenshot 2025-11-05 123045.png`
Static documentation asset illustrating the live rendered Gradio user interface, including input text fields, dropdown selectors, and output response formatting.

---

##  Technical Specifications & Stack

| Layer | Technology | Specification | Function in Repository |
|---|---|---|---|
| **Frontend Framework** | Gradio | `v4.28.3` | Renders interactive browser components (Textboxes, Dropdowns) |
| **Backend Framework** | FastAPI | Latest | Application wrapper and ASGI endpoint host |
| **ASGI Web Server** | Uvicorn | Standard | Handles asynchronous web requests on port `8000` |
| **HTTP Client** | Requests | Latest | Transmits JSON payloads to local Ollama daemon |
| **Inference Engine** | Ollama | Local Service | Serves LLM endpoints locally at `http://localhost:11434` |
| **Target Model** | Qwen | `qwen:0.5b` | 500M parameter open-weights language model |

---


