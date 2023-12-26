from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import openai
from starlette import status
import time, datetime

from database import get_db
from domain  import api_schema, api_crud
from models import Chat_content

openai.api_key = "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"  #윤제열 key

def get_completion_from_messages(messages, model="gpt-3.5-turbo-16k", temperature=0.5):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = temperature,
    )
    return response.choices[0].message["content"]

def summarizer(script, s_mode=None):
    messages =  [{'role':'system', 'content':system_message},
                      {'role':'user', 'content':script}]
    if s_mode == 'gpt':
       response = get_completion_from_messages(messages, temperature=0)
    else:
       response = '<<< == summarized for testing mode == >>> \n' + script 
    return response

system_message = """
    You act as a professional in summarizing dialogues and/or scripts.
    You will be given a chat script bewteen contact center agent and customer.
    You do the following tasks:
      1. Make a brief summary list of customer questions in Korean
      2. Make a brief summary list of agent answers in Korean.
      3. Evaluate the customer's satisfaction about the agent's service quality  in  5-star rating scale.
      4. Classify the scripts as one of categories in the list of [관광지, 숙박, 쇼핑, 교통, 음식, 축제/공연,  의료관광, 레포츠, 번역, 불편신고,  공공기관, 1330, 열린 관광지, 코스 추천, 기타]
  """

router = APIRouter(
    prefix="/api",
)

from IPython.display import display, Markdown, Latex
def md_display(text:str):
    # display(Markdown(text))
    return text

# In JSON a literal line break is not allowed inside a string, it needs to be replaced by \n

@router.post("/summary", response_model = api_schema.SummaryCreateOut)
async def chat_summary(_summary_create: api_schema.SummaryCreateIn):
    s_mode = _summary_create.mode
    start = time.time()

    summary = summarizer(_summary_create.content, s_mode)

    _summary_create.content =  md_display(summary+'\n\n\n')
    end = time.time()
    print(f' elasped time = {end - start:.5f} sec === {_summary_create.content}' )

    return {"content": _summary_create.content,
            "create_date": datetime.datetime.now()
        }
    
# get test
@router.get("/summaryGet/{content}")
async def chat_summary_get(content: str):
    start = time.time()
    summary = summarizer(content)
    summary =  md_display(summary+'\n\n\n')
    end = time.time()
   # format datetime
    print(f' elasped time = {end - start:.5f} sec')
    return summary

@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
def chat_summary_create(_content_create: api_schema.SummaryCreate,
                   db: Session = Depends(get_db)):
    # print(_content_create)
    api_crud.create_content(db = db, content_create = _content_create)