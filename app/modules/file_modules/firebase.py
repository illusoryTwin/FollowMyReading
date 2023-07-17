import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import uuid

# Firebase initialization
cred = credentials.Certificate('app/modules/file_modules/follow-my-reading-firebase-adminsdk-4h09a-362ca78573.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'follow-my-reading.appspot.com'
})
bucket = storage.bucket()


# Function to upload file to firebase storage
def firebase_upload_file(local_path):
    firebase_filename = str(uuid.uuid4().hex)  # Generate a random unique ID
    blob = bucket.blob(firebase_filename)
    blob.upload_from_filename(local_path)
    return "https://firebasestorage.googleapis.com/v0/b/follow-my-reading.appspot.com/o/" + \
        firebase_filename.replace("/", "%2F") + "?alt=media"
