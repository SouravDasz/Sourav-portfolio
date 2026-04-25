from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from app.routes.home import templates

router=APIRouter()

#project list 
projects = [
    {
        "slug": "eda-tool",
        "title": "Automated EDA Tool",
        "desc": "Generate insights and visualizations from datasets",
        "tech": ["Python", "Pandas", "Flask", "NumPy", "Matplotlib", "Seaborn"],
        "github": "https://github.com/SouravDasz/Auto-EDA",
        "demo": "https://auto-eda.onrender.com/"
    },
    {
        "slug": "ai-loan",
        "title": "AI Loan Prediction System",
        "desc": "Predicts loan eligibility using machine learning models",
        "tech": ["ML", "Python", "Flask", "SQLite", "HTML", "CSS"],
        "github": "https://github.com/SouravDasz/Bank-Loan-classifier.git",
        "demo": "https://ai-loan-prediction.onrender.com/"
    },
    {
        "slug": "dt-viewer",
        "title": "Decision Tree Visualizer",
        "desc": "Interactive tool to understand Decision Trees and hyperparameters",
        "tech": ["ML", "Python", "Flask", "Decision Trees", "HTML", "CSS"],
        "github": "https://github.com/SouravDasz/DT-VIEWER",
        "demo": None
    },
    {
        "slug": "mask-detection",
        "title": "Face Mask Detection",
        "desc": "Computer vision model to detect face mask usage in real-time",
        "tech": ["Computer Vision", "Python", "OpenCV", "Deep Learning"],
        "github": "https://github.com/SouravDasz/Mask-dection",
        "demo": None
    },
    {
        "slug": "license-plate",
        "title": "License Plate Recognition",
        "desc": "Detects and reads vehicle license plates using computer vision",
        "tech": ["Computer Vision", "Python", "OCR", "OpenCV"],
        "github": "https://github.com/SouravDasz/License-Plate-Recognition",
        "demo": None
    },
    {
        "slug": "fake-news",
        "title": "Fake News Detection",
        "desc": "ML model to classify news as real or fake",
        "tech": ["Machine Learning", "NLP", "Flask", "Python"],
        "github": "https://github.com/SouravDasz/Flask-fake-news-app.git",
        "demo": None
    },
    {
        "slug": "emotion-detector",
        "title": "Emotion Detection System",
        "desc": "Detects human emotions from facial expressions",
        "tech": ["Computer Vision", "Deep Learning", "Python", "OpenCV"],
        "github": "https://github.com/SouravDasz/Emotion-detector.git",
        "demo": None
    },
    {
        "slug": "sentiment-analysis",
        "title": "Sentiment Analysis Tool",
        "desc": "Analyzes text sentiment using NLP techniques",
        "tech": ["NLP", "Python", "Machine Learning"],
        "github": "https://github.com/SouravDasz/sentiment-analysis-tool",
        "demo": None
    }
]

@router.get("/projects")
def project(request:Request):
    return templates.TemplateResponse(request,"project.html",{"projects":projects})