# Quick Start Guide: Applied AI in People Data

## 🚀 Getting Started in 5 Minutes

This guide will help you quickly set up and start using AI-powered People Data analytics.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Basic understanding of Python
- (Optional) OpenAI API key for LLM features

## Installation

### Step 1: Clone or Download the Repository

```bash
cd peopledata
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install basic requirements
pip install -r requirements-ai.txt

# Download spaCy language model
python -m spacy download en_core_web_sm
```

### Step 4: Set Up Environment Variables (Optional for LLM features)

Create a `.env` file in the project root:

```bash
# .env
OPENAI_API_KEY=your_api_key_here
```

## Quick Examples

### Example 1: Resume Parsing (No API Required)

```python
from resume_parser import ResumeParser

# Initialize parser
parser = ResumeParser()

# Sample resume text
resume = """
John Doe
john.doe@email.com | +1-555-123-4567

EXPERIENCE:
Senior Data Scientist at TechCorp (2020 - Present)

SKILLS: Python, Machine Learning, SQL, TensorFlow
"""

# Define your skill database
skills_db = ["Python", "Machine Learning", "SQL", "TensorFlow", 
             "Java", "AWS", "Docker"]

# Parse resume
result = parser.parse_resume(resume, skills_db)
print(result)
```

**Output:**
```json
{
  "email": "john.doe@email.com",
  "phone": "+1-555-123-4567",
  "skills": ["Python", "Machine Learning", "SQL", "TensorFlow"],
  "experience": {...},
  "education": [...]
}
```

### Example 2: Semantic Skill Matching (No API Required)

```python
from skill_matcher import SkillMatcher

# Initialize matcher
matcher = SkillMatcher()

# Find similar skills
candidate_skills = ["Python", "Machine Learning", "Data Analysis"]
job_requirements = ["Python Programming", "ML Engineering", "Statistical Analysis"]

match_result = matcher.match_candidate_to_job(
    candidate_skills, 
    job_requirements
)

print(f"Match Score: {match_result['overall_score']}%")
print(f"Recommendation: {match_result['recommendation']}")
```

### Example 3: Employee Turnover Prediction

```python
import pandas as pd
from turnover_predictor import TurnoverPredictor

# Load your employee data
employee_data = pd.read_csv('employee_data.csv')

# Initialize and train predictor
predictor = TurnoverPredictor()
X, y = predictor.prepare_data(employee_data)
metrics = predictor.train(X, y)

print(f"Model Accuracy: {metrics['accuracy']:.2%}")
print(f"ROC-AUC Score: {metrics['roc_auc']:.3f}")

# Predict for new employee
new_employee = pd.DataFrame([{
    'satisfaction_level': 0.35,
    'last_evaluation': 0.85,
    'number_project': 6,
    'average_monthly_hours': 280,
    'time_spend_company': 4,
    'work_accident': 0,
    'promotion_last_5years': 0,
    'department': 'technical',
    'salary': 'low'
}])

risk = predictor.predict_turnover_risk(new_employee)
print(f"Turnover Risk: {risk['turnover_probability'].values[0]:.1%}")
```

### Example 4: Sentiment Analysis of Employee Feedback

```python
from feedback_analyzer import FeedbackAnalyzer

analyzer = FeedbackAnalyzer()

feedback_list = [
    {
        'id': 'F001',
        'employee_id': 'E001',
        'text': 'Love the flexible work hours and remote options!',
        'date': '2024-01-15'
    },
    {
        'id': 'F002',
        'employee_id': 'E002',
        'text': 'Disappointed with lack of career growth opportunities.',
        'date': '2024-01-16'
    }
]

# Analyze feedback
results = analyzer.analyze_bulk_feedback(feedback_list)

# Generate insights report
report = analyzer.generate_insights_report(results)
print(f"Positive Rate: {report['summary']['positive_rate']}%")
print(f"Recommendations: {report['recommendations']}")
```

### Example 5: Bias Detection in Job Descriptions

```python
from fairness_analyzer import FairnessAnalyzer

analyzer = FairnessAnalyzer()

jd_text = """
We're looking for a young, energetic rockstar developer.
Must be aggressive and competitive with extensive experience.
"""

bias_report = analyzer.detect_language_bias(jd_text)
print(f"Bias Score: {bias_report['bias_score']}")
print(f"Detected Issues: {bias_report['detected_bias']}")
print(f"Suggestions: {bias_report['suggestions']}")
```

## Project Structure

```
peopledata/
├── 5. Applied AI in People Data.md  # Complete documentation
├── requirements-ai.txt               # Python dependencies
├── QUICKSTART_AI.md                 # This file
├── examples/                        # Example scripts
│   ├── resume_parsing_demo.py
│   ├── skill_matching_demo.py
│   ├── turnover_prediction_demo.py
│   └── sentiment_analysis_demo.py
├── src/                            # Source code (to be organized)
│   ├── nlp/
│   │   ├── resume_parser.py
│   │   ├── job_description_analyzer.py
│   │   └── sentiment_analyzer.py
│   ├── ml/
│   │   ├── turnover_predictor.py
│   │   ├── skill_matcher.py
│   │   └── candidate_screener.py
│   └── fairness/
│       └── fairness_analyzer.py
└── data/                           # Sample data
    ├── sample_resumes.csv
    ├── sample_employees.csv
    └── skill_database.json
```

## Common Use Cases

### 1. **Automated Resume Screening**
**Time Saved:** 70-80% of manual screening time

```python
# Screen 1000 resumes in minutes
candidates = load_resumes('resumes.csv')
screener = CandidateScreener()
results = screener.screen_multiple_candidates(candidates, criteria)
top_10 = results.head(10)
```

### 2. **Proactive Retention Management**
**Impact:** Reduce turnover by 15-25%

```python
# Identify at-risk employees weekly
at_risk = predictor.predict_turnover_risk(current_employees)
high_risk = at_risk[at_risk['risk_level'] == 'High']
# Trigger retention interventions
```

### 3. **Data-Driven Hiring Decisions**
**Improvement:** 30-40% better quality of hire

```python
# Match candidates to roles semantically
matches = matcher.match_candidate_to_job(
    candidate_skills, 
    job_requirements
)
# Focus on top matches
```

### 4. **Continuous Employee Sentiment Monitoring**
**Value:** Real-time insights into employee satisfaction

```python
# Analyze feedback continuously
weekly_feedback = get_feedback(last_7_days=True)
sentiment_trends = analyzer.analyze_bulk_feedback(weekly_feedback)
# Alert on negative trends
```

## Advanced Features

### Using LLMs for Enhanced Analysis (Requires OpenAI API)

```python
from llm_resume_analyzer import LLMResumeAnalyzer

# Initialize with API key
analyzer = LLMResumeAnalyzer(api_key="your_key")

# Advanced parsing with context understanding
structured_data = analyzer.extract_structured_data(resume_text)

# Intelligent job matching
match_results = analyzer.match_job_to_resume(resume, job_description)

# Generate personalized interview questions
questions = analyzer.generate_interview_questions(resume, "Senior Engineer")
```

### Fairness Monitoring in Production

```python
from model_monitor import ModelMonitor

monitor = ModelMonitor('candidate_screener_v1')

# Log every prediction
for candidate in candidates:
    prediction = model.predict(candidate)
    monitor.log_prediction(
        prediction=prediction,
        actual=None,  # Will be filled when outcome known
        features=candidate.to_dict()
    )

# Weekly drift detection
drift_report = monitor.calculate_drift()
if drift_report['alert']:
    send_alert("Model drift detected - retrain required")
```

## Performance Optimization

### For Large-Scale Processing

```python
from scalable_processor import ScalableProcessor

# Process millions of records efficiently
for chunk in ScalableProcessor.process_in_chunks(
    'large_dataset.csv',
    process_func=parse_resume,
    chunksize=10000
):
    save_results(chunk)
```

### Parallel Processing

```python
# Use multiple CPU cores
results = ScalableProcessor.parallel_process(
    data=resume_list,
    process_func=parse_resume,
    n_workers=8
)
```

## Troubleshooting

### Common Issues

**1. "Model not found" error with spaCy**
```bash
python -m spacy download en_core_web_sm
```

**2. Out of memory errors**
```python
# Process in smaller chunks
chunksize = 1000  # Reduce if needed
```

**3. Slow inference with transformers**
```python
# Use smaller models
matcher = SkillMatcher(model_name='all-MiniLM-L6-v2')  # Faster
# Instead of 'all-mpnet-base-v2'  # More accurate but slower
```

**4. OpenAI API rate limits**
```python
import time
# Add delays between requests
time.sleep(1)
```

## Best Practices

### 1. **Data Privacy**
```python
# Always anonymize before processing
from data_anonymizer import DataAnonymizer
anon_data = DataAnonymizer.anonymize_dataframe(
    df, 
    pii_columns=['email', 'name', 'phone']
)
```

### 2. **Bias Monitoring**
```python
# Regular fairness audits
fairness_report = analyzer.analyze_hiring_bias(
    candidates_df,
    protected_attribute='gender'
)
```

### 3. **Human-in-the-Loop**
```python
# Never fully automate high-stakes decisions
if prediction_confidence < 0.85:
    flag_for_manual_review(candidate)
```

### 4. **Model Versioning**
```python
# Save models with versions
predictor.save_model('models/turnover_v2.1.pkl')
```

## Next Steps

1. **Read the full documentation**: `5. Applied AI in People Data.md`
2. **Explore example notebooks**: Check `examples/` directory
3. **Customize for your use case**: Adapt code to your data structure
4. **Join the community**: Contribute improvements and share learnings
5. **Deploy to production**: Follow deployment guide in main docs

## Getting Help

- **Documentation**: See `5. Applied AI in People Data.md`
- **Issues**: Open a GitHub issue
- **Discussions**: Join community discussions
- **Email**: vfaraji89@gmail.com

## Resources

- [spaCy Documentation](https://spacy.io/)
- [Sentence Transformers](https://www.sbert.net/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Fairness in ML](https://fairmlbook.org/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

---

**Happy Analyzing! 🚀**

*Remember: AI augments human decision-making in HR—it doesn't replace it. Always maintain ethical standards and human oversight.*
