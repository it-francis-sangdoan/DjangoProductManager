import pyrebase
import os
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

load_dotenv()

def get_firebase_storage():
    FIREBASE_CONFIG = {
        "apiKey": os.getenv("FIREBASE_API_KEY"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.getenv("FIREBASE_APP_ID"),
        "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
        "databaseURL": os.getenv("FIREBASE_DATABASE_URL")
    }
    firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
    return firebase.storage()

def upload_image_to_firebase(image_file, upload_path, image_name):

    try:
        _, file_extension = os.path.splitext(image_file.name)
        # Combine new filename with the original file extension
        file_name = f"{image_name}{file_extension}"
        # file_name = image_file.name
        file_path = default_storage.save(file_name, ContentFile(image_file.read()))
        storage = get_firebase_storage()

        # Upload file to the specified path in Firebase Storage
        storage.child(f"{upload_path}/{file_name}").put(file_path)
        file_url = storage.child(f"{upload_path}/{file_name}").get_url(None)
        return file_url
    except Exception as e:
        raise Exception(f"An error occurred while uploading the file: {str(e)}")
    finally:
        default_storage.delete(file_path)
