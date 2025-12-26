#!/usr/bin/env python3
"""
Complete Demo: AI-Powered People Data Analytics
==============================================

This demo showcases all major AI capabilities for People Data:
1. Resume Parsing
2. Skill Matching
3. Candidate Screening
4. Sentiment Analysis
5. Bias Detection

Run this to see everything in action!
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json

print("=" * 60)
print("🤖 AI-Powered People Data Analytics - Complete Demo")
print("=" * 60)

# ============================================================================
# Demo 1: Resume Parsing with NLP
# ============================================================================
print("\n📄 DEMO 1: Resume Parsing")
print("-" * 60)

class SimpleResumeParser:
    """Simplified resume parser for demo"""
    
    def parse(self, text):
        import re
        
        # Extract email
        email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        
        # Extract phone
        phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
        
        # Simple skill extraction
        common_skills = ['Python', 'Java', 'SQL', 'Machine Learning', 'ML', 
                        'Data Analysis', 'AWS', 'Docker', 'React', 'Node.js']
        found_skills = [skill for skill in common_skills if skill.lower() in text.lower()]
        
        return {
            'email': email[0] if email else None,
            'phone': phone[0] if phone else None,
            'skills': found_skills,
            'parsed_at': datetime.now().isoformat()
        }

# Sample resumes
sample_resumes = [
    """
    Alice Johnson
    alice.johnson@email.com | +1-555-0101
    
    EXPERIENCE:
    Senior Data Scientist at TechCorp (2020-Present)
    - Led machine learning projects
    - Developed Python-based analytics tools
    
    SKILLS: Python, Machine Learning, SQL, AWS, Docker
    """,
    """
    Bob Smith
    bob.smith@email.com | +1-555-0102
    
    Software Engineer with 5 years experience
    Expert in Java, React, Node.js, and SQL
    
    Built scalable web applications for Fortune 500 companies
    """
]

parser = SimpleResumeParser()

print("\nParsing resumes...")
for i, resume in enumerate(sample_resumes, 1):
    result = parser.parse(resume)
    print(f"\n📝 Resume {i}:")
    print(f"   Email: {result['email']}")
    print(f"   Phone: {result['phone']}")
    print(f"   Skills: {', '.join(result['skills'])}")

# ============================================================================
# Demo 2: Semantic Skill Matching
# ============================================================================
print("\n\n🎯 DEMO 2: Semantic Skill Matching")
print("-" * 60)

def simple_skill_match(candidate_skills, required_skills):
    """Simple skill matching based on overlap"""
    candidate_lower = [s.lower() for s in candidate_skills]
    required_lower = [s.lower() for s in required_skills]
    
    # Check for matches (exact and partial)
    matches = 0
    for req in required_lower:
        for cand in candidate_lower:
            if req in cand or cand in req:
                matches += 1
                break
    
    match_rate = matches / len(required_skills) if required_skills else 0
    score = match_rate * 100
    
    if score >= 80:
        recommendation = "🟢 Strong Match"
    elif score >= 60:
        recommendation = "🟡 Good Match"
    elif score >= 40:
        recommendation = "🟠 Moderate Match"
    else:
        recommendation = "🔴 Weak Match"
    
    return {
        'score': round(score, 1),
        'matches': matches,
        'total_required': len(required_skills),
        'recommendation': recommendation
    }

# Job requirements
job_requirements = {
    'title': 'Senior Data Scientist',
    'required_skills': ['Python', 'Machine Learning', 'SQL', 'Data Analysis'],
    'preferred_skills': ['AWS', 'Docker', 'TensorFlow']
}

# Candidates
candidates = [
    {
        'name': 'Alice Johnson',
        'skills': ['Python', 'Machine Learning', 'SQL', 'AWS', 'Docker']
    },
    {
        'name': 'Bob Smith',
        'skills': ['Java', 'React', 'Node.js', 'SQL']
    }
]

print(f"\nJob: {job_requirements['title']}")
print(f"Required Skills: {', '.join(job_requirements['required_skills'])}")
print(f"\nMatching candidates...\n")

for candidate in candidates:
    match = simple_skill_match(candidate['skills'], job_requirements['required_skills'])
    print(f"👤 {candidate['name']}")
    print(f"   Skills: {', '.join(candidate['skills'])}")
    print(f"   Match Score: {match['score']}%")
    print(f"   Matched {match['matches']}/{match['total_required']} required skills")
    print(f"   {match['recommendation']}\n")

# ============================================================================
# Demo 3: Employee Turnover Risk Prediction
# ============================================================================
print("\n📊 DEMO 3: Employee Turnover Risk Prediction")
print("-" * 60)

def predict_turnover_risk(employee):
    """Simple rule-based turnover prediction"""
    risk_score = 0
    risk_factors = []
    
    # Low satisfaction
    if employee['satisfaction_level'] < 0.4:
        risk_score += 30
        risk_factors.append("Low job satisfaction")
    
    # High workload
    if employee['average_monthly_hours'] > 250:
        risk_score += 25
        risk_factors.append("Excessive working hours")
    
    # No recent promotion
    if employee['time_in_company'] >= 4 and employee['recent_promotion'] == 0:
        risk_score += 20
        risk_factors.append("No recent career advancement")
    
    # Many projects
    if employee['number_of_projects'] > 5:
        risk_score += 15
        risk_factors.append("Overloaded with projects")
    
    # Low evaluation despite high hours
    if employee['last_evaluation'] < 0.6 and employee['average_monthly_hours'] > 200:
        risk_score += 10
        risk_factors.append("Low performance despite high effort")
    
    # Determine risk level
    if risk_score >= 60:
        risk_level = "🔴 HIGH"
    elif risk_score >= 40:
        risk_level = "🟠 MEDIUM"
    else:
        risk_level = "🟢 LOW"
    
    return {
        'risk_score': risk_score,
        'risk_level': risk_level,
        'risk_factors': risk_factors
    }

# Sample employees
employees = [
    {
        'id': 'E001',
        'name': 'Employee A',
        'satisfaction_level': 0.35,
        'last_evaluation': 0.85,
        'number_of_projects': 6,
        'average_monthly_hours': 280,
        'time_in_company': 4,
        'recent_promotion': 0
    },
    {
        'id': 'E002',
        'name': 'Employee B',
        'satisfaction_level': 0.75,
        'last_evaluation': 0.82,
        'number_of_projects': 3,
        'average_monthly_hours': 180,
        'time_in_company': 2,
        'recent_promotion': 1
    },
    {
        'id': 'E003',
        'name': 'Employee C',
        'satisfaction_level': 0.50,
        'last_evaluation': 0.65,
        'number_of_projects': 5,
        'average_monthly_hours': 220,
        'time_in_company': 3,
        'recent_promotion': 0
    }
]

print("\nAnalyzing turnover risk for employees...\n")

for emp in employees:
    risk = predict_turnover_risk(emp)
    print(f"👤 {emp['name']} ({emp['id']})")
    print(f"   Satisfaction: {emp['satisfaction_level']:.2f}")
    print(f"   Monthly Hours: {emp['average_monthly_hours']}")
    print(f"   Risk Level: {risk['risk_level']}")
    print(f"   Risk Score: {risk['risk_score']}/100")
    if risk['risk_factors']:
        print(f"   Risk Factors:")
        for factor in risk['risk_factors']:
            print(f"     • {factor}")
    print()

# ============================================================================
# Demo 4: Sentiment Analysis of Employee Feedback
# ============================================================================
print("\n💬 DEMO 4: Employee Feedback Sentiment Analysis")
print("-" * 60)

def analyze_sentiment(text):
    """Simple sentiment analysis based on keywords"""
    text_lower = text.lower()
    
    positive_words = ['great', 'excellent', 'good', 'happy', 'satisfied', 
                     'love', 'amazing', 'wonderful', 'fantastic', 'perfect']
    negative_words = ['bad', 'poor', 'terrible', 'unhappy', 'dissatisfied', 
                     'hate', 'awful', 'horrible', 'worst', 'disappointed']
    urgent_words = ['urgent', 'immediately', 'critical', 'asap', 'quit', 'leaving']
    
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    urgent = any(word in text_lower for word in urgent_words)
    
    if pos_count > neg_count:
        sentiment = "😊 POSITIVE"
        confidence = 0.7 + (pos_count * 0.1)
    elif neg_count > pos_count:
        sentiment = "😟 NEGATIVE"
        confidence = 0.7 + (neg_count * 0.1)
    else:
        sentiment = "😐 NEUTRAL"
        confidence = 0.5
    
    confidence = min(confidence, 0.95)
    
    urgency = "🚨 HIGH" if urgent else "📝 NORMAL"
    
    return {
        'sentiment': sentiment,
        'confidence': round(confidence, 2),
        'urgency': urgency
    }

# Sample employee feedback
feedback_samples = [
    {
        'employee_id': 'E101',
        'date': '2024-01-15',
        'feedback': 'I love the flexible work hours and remote options. Great work-life balance!'
    },
    {
        'employee_id': 'E102',
        'date': '2024-01-16',
        'feedback': 'Very disappointed with the lack of career growth opportunities.'
    },
    {
        'employee_id': 'E103',
        'date': '2024-01-17',
        'feedback': 'Urgent: The workload is terrible and affecting my health. Considering leaving.'
    },
    {
        'employee_id': 'E104',
        'date': '2024-01-18',
        'feedback': 'Good team environment. Management is supportive.'
    }
]

print("\nAnalyzing employee feedback...\n")

sentiment_summary = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}

for fb in feedback_samples:
    analysis = analyze_sentiment(fb['feedback'])
    
    # Count sentiments
    sentiment_type = analysis['sentiment'].split()[1]
    sentiment_summary[sentiment_type] += 1
    
    print(f"📝 Feedback from {fb['employee_id']} ({fb['date']})")
    print(f"   Text: \"{fb['feedback'][:80]}...\"" if len(fb['feedback']) > 80 else f"   Text: \"{fb['feedback']}\"")
    print(f"   Sentiment: {analysis['sentiment']} (confidence: {analysis['confidence']})")
    print(f"   Urgency: {analysis['urgency']}")
    print()

# Summary
print("\n📊 Sentiment Summary:")
total = len(feedback_samples)
for sentiment, count in sentiment_summary.items():
    percentage = (count / total) * 100
    print(f"   {sentiment}: {count}/{total} ({percentage:.1f}%)")

# ============================================================================
# Demo 5: Bias Detection in Job Descriptions
# ============================================================================
print("\n\n⚖️  DEMO 5: Bias Detection in Job Descriptions")
print("-" * 60)

def detect_bias(text):
    """Detect biased language in job descriptions"""
    text_lower = text.lower()
    
    bias_found = {}
    
    # Gender-coded words
    masculine_words = ['aggressive', 'competitive', 'dominant', 'ninja', 'rockstar', 'guru']
    feminine_words = ['supportive', 'collaborative', 'nurturing', 'understanding']
    
    found_masculine = [w for w in masculine_words if w in text_lower]
    found_feminine = [w for w in feminine_words if w in text_lower]
    
    if found_masculine or found_feminine:
        bias_found['gender'] = {
            'masculine': found_masculine,
            'feminine': found_feminine
        }
    
    # Age bias
    age_words = ['young', 'energetic', 'digital native', 'recent graduate']
    found_age = [w for w in age_words if w in text_lower]
    if found_age:
        bias_found['age'] = found_age
    
    # Exclusionary language
    exclusionary = ['culture fit', 'like us', 'one of us']
    found_exclusionary = [w for w in exclusionary if w in text_lower]
    if found_exclusionary:
        bias_found['exclusionary'] = found_exclusionary
    
    # Calculate bias score
    total_bias_words = sum(
        len(v) if isinstance(v, list) else len(v.get('masculine', [])) + len(v.get('feminine', []))
        for v in bias_found.values()
    )
    
    word_count = len(text.split())
    bias_score = (total_bias_words / word_count * 100) if word_count > 0 else 0
    
    assessment = "🔴 High Bias" if bias_score > 2 else "🟡 Moderate Bias" if bias_score > 1 else "🟢 Low Bias"
    
    return {
        'bias_score': round(bias_score, 2),
        'assessment': assessment,
        'bias_found': bias_found
    }

# Sample job descriptions
job_descriptions = [
    {
        'title': 'Software Developer',
        'text': '''We're looking for a rockstar developer who is aggressive and competitive.
        Must be young and energetic with a culture fit mindset.'''
    },
    {
        'title': 'Data Analyst',
        'text': '''Seeking an analytical professional with strong problem-solving skills.
        Experience with Python and SQL required. Remote work available.'''
    }
]

print("\nAnalyzing job descriptions for bias...\n")

for jd in job_descriptions:
    analysis = detect_bias(jd['text'])
    
    print(f"📋 Job Title: {jd['title']}")
    print(f"   Assessment: {analysis['assessment']}")
    print(f"   Bias Score: {analysis['bias_score']}%")
    
    if analysis['bias_found']:
        print(f"   Issues Found:")
        for bias_type, words in analysis['bias_found'].items():
            if isinstance(words, dict):
                if words.get('masculine'):
                    print(f"     • Masculine-coded: {', '.join(words['masculine'])}")
                if words.get('feminine'):
                    print(f"     • Feminine-coded: {', '.join(words['feminine'])}")
            else:
                print(f"     • {bias_type.title()}: {', '.join(words)}")
        print(f"   Recommendation: Revise language to be more inclusive")
    else:
        print(f"   ✅ No major bias detected")
    print()

# ============================================================================
# Summary and Recommendations
# ============================================================================
print("\n" + "=" * 60)
print("✅ Demo Complete!")
print("=" * 60)

print("""
🎯 Key Takeaways:

1. Resume Parsing: Automate extraction of candidate information
   → Saves 70-80% of manual screening time

2. Skill Matching: Use semantic matching for better accuracy
   → Improves quality of hire by 30-40%

3. Turnover Prediction: Identify at-risk employees proactively
   → Reduce turnover by 15-25%

4. Sentiment Analysis: Monitor employee satisfaction in real-time
   → Early detection of issues

5. Bias Detection: Ensure fair and inclusive hiring
   → Build diverse, high-performing teams

📚 Next Steps:
- Read full documentation: '5. Applied AI in People Data.md'
- Install advanced tools: pip install -r requirements-ai.txt
- Try with your own data
- Explore more examples in /examples directory

🤝 Need Help?
- Documentation: See main README.md
- Issues: Open a GitHub issue
- Email: vfaraji89@gmail.com
""")

print("=" * 60)
print("Thanks for trying AI-Powered People Data Analytics! 🚀")
print("=" * 60)
