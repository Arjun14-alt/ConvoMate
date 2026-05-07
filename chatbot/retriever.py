from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chatbot.knowledge_base import load_knowledge

# Load dataset
questions, answers = load_knowledge()

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_best_match(user_input):
    user_vec = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vec, question_vectors)

    index = similarity.argmax()
    score = similarity[0][index]

    # fallback if no good match
    if score < 0.2:
        return "Sorry, I don't know that yet. Try asking something else."

    return answers[index]