from fastapi import FastAPI
import openai
from pydantic import BaseModel


class Question(BaseModel):
    question: str

app = FastAPI()


@app.get("/")
def read_root():

    return {"Sucess": True}


@app.post("/question/")
async def create_item(question: Question):
    print("vo")
    openai.api_key = ""
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"De modo simples,como fazer uma {question.question}",
                temperature=0.15,
                max_tokens=1000,
                top_p=1,
                #   frequency_penalty=0.0,
                #   presence_penalty=0.6,
                stop=[" Human:", " AI:"]
                )
    print("busquei")
    return {"Hello": response["choices"][0]["text"]}