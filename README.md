# Qwen AI Chatbot with RAG Integration

A sophisticated conversational AI application built with Qwen 3 (0.6B) model, featuring web-based chat interface and extensible architecture for Retrieval-Augmented Generation (RAG) capabilities.

## 🚀 Features

- **Advanced Language Model**: Powered by Qwen 3 (0.6B) from Alibaba's Qwen family
- **Interactive Web Interface**: Clean, responsive chat UI built with Flask
- **Conversation Memory**: Maintains context across chat sessions
- **RESTful API**: Well-structured endpoints for easy integration
- **RAG-Ready Architecture**: Designed for seamless integration with LangChain and vector databases
- **Cross-Origin Support**: CORS-enabled for frontend flexibility

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Flask API      │    │   Qwen Model    │
│   (Web UI)      │◄──►│   (app.py)       │◄──►│   (qwen3.py)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   Future RAG     │
                       │   Integration    │
                       │   (LangChain)    │
                       └──────────────────┘
```

## 📋 Prerequisites

- Python 3.8+
- pip package manager
- Internet connection (for model download)
- Minimum 4GB RAM recommended

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd qwen-ai-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create requirements.txt** (if not exists)
   ```text
   flask==2.3.3
   flask-cors==4.0.0
   transformers==4.35.0
   torch==2.1.0
   kagglehub==0.2.0
   langchain==0.0.350
   langchain-community==0.0.10
   ```

## 🚀 Quick Start

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:3000`
   - Start chatting with the AI assistant

3. **API Usage**
   ```bash
   curl -X POST http://localhost:3000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, how are you?"}'
   ```

## 🔗 API Endpoints

### Chat Endpoint
- **URL**: `/chat`
- **Method**: `POST`
- **Content-Type**: `application/json`

**Request Body:**
```json
{
  "message": "Your question here"
}
```

**Response:**
```json
{
  "response": "AI generated response"
}
```

**Error Response:**
```json
{
  "error": "Error description"
}
```

## 🧠 Model Information

**Qwen 3 (0.6B Model)**
- **Developer**: Alibaba Cloud
- **Model Size**: 0.6 billion parameters
- **Use Case**: Lightweight conversational AI
- **Languages**: Primarily English and Chinese
- **Context Length**: Optimized for multi-turn conversations

## 🔄 RAG Integration Roadmap

### Phase 1: Document Processing
- [ ] PDF document ingestion
- [ ] Text chunking and preprocessing
- [ ] Vector embeddings generation

### Phase 2: Vector Database
- [ ] ChromaDB integration
- [ ] Semantic search implementation
- [ ] Document retrieval optimization

### Phase 3: LangChain Integration
```python
# Future implementation example
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

class RAGQwenChatbot(QwenChatbot):
    def __init__(self, vector_store_path=None):
        super().__init__()
        self.setup_rag_pipeline(vector_store_path)
    
    def setup_rag_pipeline(self, vector_store_path):
        embeddings = HuggingFaceEmbeddings()
        self.vector_store = Chroma(
            persist_directory=vector_store_path,
            embedding_function=embeddings
        )
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.model,
            retriever=self.vector_store.as_retriever()
        )
```

## 📁 Project Structure

```
qwen-ai-chatbot/
├── app.py                 # Flask web application
├── qwen3.py              # Qwen model wrapper
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   └── index.html       # Main chat interface
├── static/              # Static assets (CSS, JS)
│   ├── style.css       # Styling
│   └── script.js       # Frontend logic
├── docs/               # Documentation
└── tests/              # Unit tests
```

## ⚙️ Configuration

### Environment Variables
```bash
export QWEN_MODEL_PATH=/path/to/model  # Optional: custom model path
export FLASK_ENV=development          # Development mode
export FLASK_DEBUG=True              # Enable debug mode
```

### Model Configuration
```python
# In qwen3.py - customize generation parameters
response_ids = self.model.generate(
    **inputs, 
    max_new_tokens=512,      # Adjust response length
    temperature=0.7,         # Control creativity
    top_p=0.9,              # Nucleus sampling
    do_sample=True          # Enable sampling
)
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

Test the API endpoint:
```bash
python -m unittest tests.test_api
```

## 📊 Performance Optimization

### Memory Management
- Model uses approximately 1.2GB RAM
- Conversation history is stored in memory
- Consider implementing conversation pruning for long sessions

### Response Time
- Average response time: 2-3 seconds
- GPU acceleration recommended for production
- Batch processing for multiple requests

## 🔒 Security Considerations

- Input validation implemented for chat endpoint
- CORS configured for controlled access
- Rate limiting recommended for production deployment
- Consider implementing user authentication

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 3000

CMD ["python", "app.py"]
```

### Production Considerations
- Use Gunicorn or uWSGI for production WSGI server
- Implement Redis for session management
- Set up reverse proxy with Nginx
- Configure SSL/TLS certificates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Alibaba Cloud** for the Qwen model family
- **Hugging Face** for the Transformers library
- **LangChain** community for RAG implementation patterns
- **Flask** team for the lightweight web framework

## 📞 Support

For questions and support:
- Create an issue in the GitHub repository
- Check the documentation in the `/docs` folder
- Review the API examples in `/examples`

## 🔄 Changelog

### v1.0.0 (Current)
- Initial release with Qwen 3 integration
- Basic web interface and REST API
- Conversation memory implementation

### v1.1.0 (Planned)
- RAG integration with LangChain
- Vector database support
- Document upload functionality

---

**Built with ❤️ using Qwen AI, Flask, and modern NLP technologies**
