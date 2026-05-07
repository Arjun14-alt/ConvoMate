def load_knowledge():
    
    data = {
        "what is dbms": "DBMS stands for Database Management System. It is used to store and manage data efficiently.",
        "explain database": "A database is an organized collection of structured information stored electronically.",
        "what is met gala": "The Met Gala is a yearly fundraising fashion event held in New York for the Costume Institute.",
        "what is python": "Python is a high-level programming language used in AI, web development, and automation.",
        "who is elon musk": "Elon Musk is an entrepreneur known for Tesla, SpaceX, and Neuralink."
    }

    questions = list(data.keys())
    answers = list(data.values())

    return questions, answers