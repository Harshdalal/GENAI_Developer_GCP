# 🤖 CrewAI Agents - Google Cloud Run Deployment

A simple web application that deploys AI agents for research and blog creation using CrewAI framework on Google Cloud Run.

## 🎯 Features

- **Research Agent**: Analyzes topics and provides detailed insights
- **Blog Creation Team**: Multi-agent workflow (Research → Write → Edit)
- **Simple UI**: Easy-to-use Streamlit interface
- **Global Access**: Public URL accessible worldwide
- **Auto-scaling**: Scales from 0 to handle any traffic
- **Cost Efficient**: Pay only when used

## 📁 Project Structure

```
ai-agents/
├── main.py              # Streamlit web interface
├── agents.py            # CrewAI agent definitions  
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
└── README.md           # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Google Cloud account (free $300 credit)
- Google Gemini API key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Step-by-Step Deployment

1. **Open Google Cloud Console**
   - Go to https://console.cloud.google.com
   - Click Cloud Shell (`>_` icon at top)

2. **Create and Setup Project Folder**
   ```bash
   mkdir ai-agents
   cd ai-agents
   ```

3. **Upload All 4 Files**
   - Drag and drop: `main.py`, `agents.py`, `Dockerfile`, `requirements.txt`
   - Verify with: `ls`

4. **Setup Project Variables**
   ```bash
   PROJECT_ID=$(gcloud config get-value project)
   PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
   echo "Project ID: $PROJECT_ID"
   echo "Project Number: $PROJECT_NUMBER"
   ```

5. **Enable Required Services**
   ```bash
   gcloud services enable cloudbuild.googleapis.com run.googleapis.com
   ```

6. **Set Permissions (One-time Setup)**
   ```bash
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
     --role="roles/run.developer"
   
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
     --role="roles/storage.admin"
   
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
     --role="roles/cloudbuild.builds.builder"
   ```

7. **Set Up Google API Key Variable**
   - Go to the Cloud Run section in the Google Cloud Console.
   - Select your `ai-agents` service or create a new one.
   - Click **Edit & Deploy New Revision**.
   - Under **Variables & Secrets**, add a new environment variable:
     - Name: `GOOGLE_API_KEY`
     - Value: Your Gemini API key (e.g., `AIzaSyACoYACs4T7NX-97k8nTpbJRdwvGHQQ`)
   - Click **Deploy** to save the configuration.

8. **Build Docker Image**
   ```bash
   docker build -t gcr.io/crew-ai-466914/ai-agents:latest .
   ```

9. **Push Docker Image to Container Registry**
   ```bash
   docker push gcr.io/crew-ai-466914/ai-agents:latest
   ```

10. **Deploy Application**
    ```bash
    gcloud run deploy ai-agents \
      --image gcr.io/crew-ai-466914/ai-agents:latest \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated
    ```

11. **Get Your Public URL**
    After 3-4 minutes, you'll receive:
    ```
    ✅ Service [ai-agents] has been deployed
    🌐 URL: https://ai-agents-xxxxx-uc.a.run.app
    ```

## 🤖 How It Works

### Research Agent
- **Input**: Any topic (e.g., "Benefits of AI in education")
- **Process**: Single agent analyzes and researches
- **Output**: Comprehensive research report with examples
- **Time**: ~30-60 seconds

### Blog Creation Team
- **Input**: Blog topic (e.g., "Future of remote work")
- **Process**: 3 agents working sequentially:
  1. 🔍 Researcher gathers information
  2. ✍️ Writer creates blog post
  3. ✏️ Editor polishes content
- **Output**: Publication-ready blog post
- **Time**: ~2-3 minutes

## 💰 Cost Breakdown

### Google Cloud Run
- **Pricing**: ~$0.40 per 1M requests
- **Free Tier**: 2M requests/month free
- **Scaling**: Automatically scales to zero (no cost when idle)

### Google Gemini API
- **Free Tier**: 15 requests/minute
- **Paid**: $0.35 per 1M input tokens
- **Typical Usage**: $0-5/month for moderate use

### Total Expected Cost
- **Light Usage**: Free (within free tiers)
- **Moderate Usage**: $1-10/month
- **Heavy Usage**: Scales with actual usage

## 🔧 Technical Details

### Environment Variables
- `GOOGLE_API_KEY`: Your Gemini API key (set during deployment in Cloud Run UI)
- `PORT`: Application port (auto-set by Cloud Run to 8501)

### API Configuration
- **Model**: `gemini/gemini-1.5-flash` (fast and cost-effective)
- **Framework**: CrewAI for multi-agent workflows
- **Interface**: Streamlit for web UI

### Container Specifications
- **Base Image**: Python 3.11 slim
- **Memory**: Auto-allocated (typically 512MB-2GB)
- **CPU**: Auto-allocated (0.1-2 vCPU)
- **Timeout**: 300 seconds (5 minutes)

## 📊 Management & Monitoring

### Useful Commands
```bash
# View application logs
gcloud run services logs read ai-agents --region=us-central1 --limit=50

# Update deployment (after code changes)
gcloud run deploy ai-agents --source . --region us-central1 --allow-unauthenticated

# Check service status
gcloud run services describe ai-agents --region=us-central1

# Scale settings
gcloud run services update ai-agents --max-instances=10 --region=us-central1

# Delete service
gcloud run services delete ai-agents --region=us-central1
```

### Monitoring Dashboard
- **URL**: https://console.cloud.google.com/run
- **Metrics**: Request count, latency, error rate
- **Logs**: Real-time application logs
- **Billing**: Cost tracking and alerts

## 🛠️ Troubleshooting

### Common Issues & Solutions

1. **Permission Denied Error**
   ```
   ERROR: Build failed because the default service account is missing required IAM permissions
   ```
   **Solution**: Run the permission commands from step 6

2. **Missing Entrypoint Error**
   ```
   failed to build: for Python, provide a main.py file
   ```
   **Solution**: Ensure main file is named `main.py` (not `app.py`)

3. **Syntax Error in agents.py**
   ```
   SyntaxError: invalid syntax
   ```
   **Solution**: Use the exact `agents.py` code provided above

4. **API Connection Error**
   ```
   Could not resolve project_id
   ```


### Error Prevention Checklist
- ✅ All 4 files uploaded correctly
- ✅ Main file named `main.py`
- ✅ Valid Gemini API key
- ✅ Services enabled
- ✅ Permissions set correctly
- ✅ Using `gemini/gemini-1.5-flash` model

## 🌐 Production Deployment

### Security Best Practices
- API key stored securely as environment variable
- No authentication required for public access
- HTTPS enabled by default
- Container runs as non-root user

### Performance Optimization
- Cold start time: 5-15 seconds
- Warm requests: <1 second response
- Concurrent users: Up to 1000 per instance
- Auto-scaling based on traffic

### Scaling Configuration
```bash
# Set custom scaling (optional)
gcloud run services update ai-agents \
  --min-instances=0 \
  --max-instances=10 \
  --concurrency=80 \
  --region=us-central1
```

## 📝 Version History

### v1.0 (Current)
- ✅ Single agent research functionality
- ✅ Multi-agent blog creation team
- ✅ Environment variable API key handling
- ✅ Fixed project_id resolution error
- ✅ Simplified Gemini API integration

## 🤝 Contributing

1. Fork this repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit Pull Request

## 📞 Support

### Getting Help
- **Documentation**: Check this README first
- **Google Cloud**: [Cloud Run Documentation](https://cloud.google.com/run/docs)
- **CrewAI**: [Official Documentation](https://docs.crewai.com)
- **Issues**: Create issue in repository

### Resources
- [Google AI Studio](https://makersuite.google.com/app/apikey) - Get API key
- [Google Cloud Console](https://console.cloud.google.com) - Manage deployment
- [CrewAI Examples](https://github.com/joaomdmoura/crewAI-examples) - More agent examples

---

**🚀 Built with CrewAI • Powered by Google Cloud Run • Designed for Global Access**

*Ready to deploy AI agents that anyone can access from anywhere in the world!*