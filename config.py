import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'speciaal-voor-munkje' #haalt environment var op, en als die niet beschikbaar is DAN iets hardcoded