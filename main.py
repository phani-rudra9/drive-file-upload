from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError as HTTPError
from googleapiclient.http import MediaFileUpload

if __name__ == '__main__':
    SCOPES = ['https://www.googleapis.com/auth/drive']

    sa_creds = service_account.Credentials.from_service_account_file('credentials.json')
    scoped_creds = sa_creds.with_scopes(SCOPES)
    drive_service = build('drive', 'v3', credentials=scoped_creds)
    file_metadata = {'name': 'meow.csv', 'mimeType': 'text/csv', 'parents': ['18yWIE9KnfphdWRUk_Q4EFrf7Kre1bO7_']}
    media = MediaFileUpload('./meow.csv', mimetype='text/csv')
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id',
                                        supportsAllDrives=True).execute()
    print('File ID: %s' % file.get('id'))
