import urequests
import ujson
from dotenv import load_dotenv
import os

def notion_push():
    load_dotenv()

    url = "https://api.notion.com/v1/pages"
    database_id = os.getenv('database_id')
    API_key = os.getenv('API_key')

    payload = {
        "parent": {"database_id":"{database_id}"},
        "properties": {
            "Name":{
                "title":[
                    {
                        "text":{
                            "content" : "トイレに行きました"
                        }
                    }
                ]
            }
        },
        "children": [
            {
                "object" : "block",
                "type"  : "paragraph",
                "paragraph":{
                    "rich_text":[
                        {
                            "text" :{
                                "content":"特にありません"
                            }
                        }
                    ]
                }
            }
        ]
        
    }

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": "{API_key}"
    }

    response = urequests.post(url, data=ujson.dumps(payload).encode("utf-8"), headers=headers)
    return response.json()