# 🧠 LangGraph AI Agent (with Streamlit + Docker)

This project is an **AI assistant** that decides **how to answer a user question** — either using:

- A calculator (for math questions), or
- A language model (for general knowledge)

Built using:
- [Streamlit](https://streamlit.io/) for the web interface
- [LangGraph](https://github.com/langchain-ai/langgraph) for decision flow
- [LangChain](https://www.langchain.com/) for AI interactions
- [gemini-1.5-flash] as the LLM

---

## What This Project Does

- User asks a question on a web page
- The agent decides:
  - If it's a math problem → uses the calculator tool
  - Else → uses gemini-1.5-flash to answer
- The answer is shown to the user with intermediate steps logged

---

## Files and What They Do

| File               | Purpose                                                   |
|--------------------|-----------------------------------------------------------|
| `app.py`           | Streamlit frontend (runs the web interface)              |
| `main.py`          | Backend logic (LangGraph, LLM, tools, decision making)   |
| `.env`             | Your Google api key (not shared publicly)                |
| `requirements.txt` | Python packages needed for the project                   |
| `Dockerfile`       | Defines how to run this project inside a Docker container|
| `.dockerignore`    | Tells Docker what files to skip (like .env)              |

---

## Requirements

You need:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- A Google API key in your .env file

---

## How to Run Without Docker (Python Only)

1. **Clone this repo or download files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env file (in the same folder):**
   ```
   GOOGLE_API_KEY= google_api_key
   ```

4. **Run the App:**
   ```bash
   streamlit run app.py
   ```
   Visit your browser: http://localhost:8501

---

## How to Run Using Docker

### Step 1: Install Docker

**For Windows:**

1. **Enable WSL2 (If not already enabled)**
   Open PowerShell as Administrator, and run:
   ```powershell
   wsl --install
   ```
   Restart your computer if prompted.

2. **Download Docker Desktop**
   Go to https://www.docker.com/products/docker-desktop/
   Download Docker Desktop for Windows.

3. **Install Docker Desktop**
   - Run the .exe installer
   - Make sure WSL2 is selected as the backend
   - Follow the instructions and finish the installation

4. **Verify Installation**
   Open a terminal (PowerShell or CMD) and run:
   ```bash
   docker --version
   docker run hello-world
   ```

### Step 2: Run the Application

1. **Add your .env file (in the project folder):**
   ```
   GOOGLE_API_KEY= google_api_key
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t langgraph-app .
   ```

3. **Run the app using Docker:**
   ```bash
   docker run --env-file .env -p 8501:8501 langgraph-app
   ```

4. **Open in browser:**
   http://localhost:8501

---

## How We Dockerized It

- Wrote a Dockerfile with:
  - Python base image
  - Copied app files
  - Installed required libraries
  - Launched Streamlit on port 8501
- Used .env file to pass GOOGLE_API_KEY= google_api_key securely

---

## Example Questions to Try

- **What is 7 * 4?** → Uses calculator
- **Who won the Nobel Peace Prize in 2020?** → Uses Gemini

---

## Deploy to Google Cloud Platform (GCP)

### Step 1: Log in to GCP Console

1. Go to https://console.cloud.google.com
2. Make sure you're in the correct project (e.g., gen-ai)
3. If not, create a project named gen-ai and then use the project selector (top nav) and switch to gen-ai

### Step 2: Enable Required APIs (Only once per project)

Go to APIs & Services and enable the following APIs:
- Cloud Run API
- Artifact Registry API
- Cloud Build API

### Step 3: Create Artifact Registry

We'll store the Docker image here.

1. Go to: **Navigation Menu > Artifact Registry > Repositories**
2. Click **"Create Repository"**
3. Fill the form:
   - **Name:** langgraph-app
   - **Format:** Docker
   - **Location Type:** Region
   - **Region:** asia-south1 (Mumbai)
4. Click **"Create"**

### Step 4: Build and Push Docker Image

**Docker image file:**

```dockerfile
# Dockerfile

# 1. Base image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Copy all files
COPY . .

# 5. Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Expose Streamlit port
EXPOSE 8080

# 7. Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

**Upload your Streamlit app as a Docker image into Artifact Registry:**

1. Make sure your Dockerfile and app.py are ready
2. In app.py, modify this part to read port from the environment (important):
   ```python
   # NOTE: Streamlit always listens on 8080
   os.environ["STREAMLIT_SERVER_PORT"] = os.environ.get("PORT", "8080")
   ```

3. Use Google Cloud Shell or CMD in your project directory:
   ```bash
   gcloud auth configure-docker asia-south1-docker.pkg.dev

   # Build Docker image
   docker build -t asia-south1-docker.pkg.dev/gen-ai-462005/langgraph-app/langgraph-app:new .

   # Push to Artifact Registry
   docker push asia-south1-docker.pkg.dev/gen-ai-462005/langgraph-app/langgraph-app:new
   ```

This stores the Docker image into your Artifact Registry.

### Step 5: Deploy to Cloud Run (GUI Only)

1. Go to: **Navigation Menu > Cloud Run**
2. Click **"Create Service"**
3. Fill in the details:
   - **Service name:** langgraph-app
   - **Deployment platform:** Fully managed
   - **Region:** asia-south1
   - **Container image URL:** Click "Select" → Artifact Registry → gen-ai-462005 → langgraph-app → langgraph-app:new
4. Click **Next**

### Step 6: Configure Service Settings

- **Port:** 8080 (this is where Streamlit runs)
- **Memory:** You can keep 512MB or more if needed
- **Environment Variables:**
  - Click "Add Variable"
  - **Name:** GOOGLE_API_KEY
  - **Value:** <google_api_key>
- **Authentication:**
  - In "Ingress and security", choose:
  - **Allow all traffic**
  - **Authentication:** Allow unauthenticated invocations

### Step 7: Review and Deploy

1. Click **Create**
2. Wait for deployment to complete
3. Once it's deployed, you'll see a URL like: `https://langgraph-app-xxxxx.a.run.app`
4. Click it – your Streamlit app should open

### Step 8: If You Get Errors

1. Go to **Cloud Run > Click on your service**
2. Use the **"Logs"** tab to debug common errors like:
   - Wrong port (should be 8080)
   - Missing GOOGLE_API_KEY
   - Python crash
3. If it says "didn't respond to PORT", it's likely:
   - The app is not using `os.environ["PORT"]` or not running at 8080
   - Fix and re-push the image