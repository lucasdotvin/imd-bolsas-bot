import os

if not os.getenv('DATABASE_URL'):
    from dotenv import load_dotenv
    load_dotenv()
