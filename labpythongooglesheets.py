from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'lab.json'
speadsheet_id = '1XyZaWORP0Tju3tKI7PTLPyGRym411Po3iktYRRhbRk4'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    scopes=['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
spreadsheet = service.spreadsheets().get(spreadsheetId = speadsheet_id).execute()
sheetList = spreadsheet.get('sheets')
sheetId = sheetList[0]['properties']['sheetId']

# values = service.spreadsheets().values().get(
#     spreadsheetId = speadsheet_id,
#     range = 'A5:C10',
#     majorDimension='COLUMNS').execute()
#
# pprint(values)


# Объединяем ячейки A2:D1
results = service.spreadsheets().batchUpdate(
    spreadsheetId = speadsheet_id,
    body = {"requests": [
            {'mergeCells': {'range': {'sheetId': sheetId,
                          'startRowIndex':3,
                          'endRowIndex': 4,
                          'startColumnIndex': 0,
                          'endColumnIndex': 4},
                'mergeType': 'MERGE_ALL'}}
        ]
    }).execute()
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId = speadsheet_id,
#     body={
#         'valueInputOption':'USER-ENTERED',
#         'data':[
#             {'range':'B63:C64',
#             'majorDimension':'ROWS',
#             'values':[['This is B63', 'This is C63'], ['This is B64', 'This is C64']]}
#         ]
#     }
# ).execute()
