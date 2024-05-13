from pydantic import BaseModel
from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


class Option(BaseModel):
    id: int
    text: str
    picture: str



from fastapi import FastAPI

app = FastAPI()

@app.get("/initiate/")
async def initiate_coverstation():
    conversation = [
        {"bot","Hi! 👋🏼 My name is Natalie and I'm your assistant here at Centre Dental. How can I help you today?"},
        {"bot","Please choose an option below"},
    ]
    return conversation



@app.get("/options/")
async def get_options():
    options = [
    Option(id=1, text="What insurance do you accept?", picture="https://media.botsrv2.com/control/img/optimized/be/a4b04b660846329a7b84d4bbbfbb45/blob.png"),
    Option(id=2, text="New Patient Special!", picture="https://media.botsrv2.com/control/img/optimized/b5/acf1a96cd149488d48c951caa3a053/blob.png"),
    Option(id=3, text="I'd like to request an appointment", picture="https://media.botsrv2.com/control/img/optimized/b5/acf1a96cd149488d48c951caa3a053/blob.png"),
    Option(id=4, text="What services do you offer?", picture="https://media.botsrv2.com/control/img/optimized/a5/f0a669b0bd445b801ba431e4ccc20e/blob.png"),
    Option(id=5, text="FAQ", picture="https://media.botsrv2.com/control/img/optimized/a5/f0a669b0bd445b801ba431e4ccc20e/blob.png"),
    Option(id=6, text="Chat with AI", picture="ai.jpg"),
    ]

    return options

@app.get("/insurance/")
async def insurance_info():
    question = [
        {"bot","We accept all PPOs, we can help claim Union plans, we cannot accept Medicaid or DMOs. In general, we are out of network providers."},
        {"bot","Would you like to request an appointment?"},
    ]

    return question


@app.post("/get_user_info/")
async def get_user_info(name: str,phone: str):
    question = [
        {"bot",f"Thank You, {name}. Your info has been stored. We will forward this to our customer support team so they can answer your queries in a better way"},
    ]

    return question


@app.get("/get_new_patient_special")
async def patient_special():
    [
        {"bot","$150 for comprehensive exam, X-rays, iTero 5D scan, and regular cleaning"},
        {"bot","All you have to do is request your appointment with us. Just tap the \"Claim Offer\" button below to get started!"},
        {"bot","Would you like to schedule an appointment online or have someone from our office call you to schedule an appointment?"},
    ]


@app.get("/servies_info")
async def services():
    services = """\
        Root Canal
        Dental Implants
        Full Mouth Reconstruction
        Teeth Whitening
        Veneers
        Invisalign
        Wisdom Teeth
        Pinhole Gum Rejuvenation
        Teeth Cleaning
        PRF Treatment
        Digital Impression
        Laser Dentistry
        Laser Snore Therapy
        """

    [
        {"bot","$150 for comprehensive exam, X-rays, iTero 5D scan, and regular cleaning"},
         {"bot",services},
    ]



@app.get("/servies_info")
async def services():
    services = """\
        Root Canal
        Dental Implants
        Full Mouth Reconstruction
        Teeth Whitening
        Veneers
        Invisalign
        Wisdom Teeth
        Pinhole Gum Rejuvenation
        Teeth Cleaning
        PRF Treatment
        Digital Impression
        Laser Dentistry
        Laser Snore Therapy
        """

    conversation = [
        {"bot","$150 for comprehensive exam, X-rays, iTero 5D scan, and regular cleaning"},
         {"bot",services},
    ]   

    return conversation


@app.post("/appointment/")
async def new_appointmnet(day:str,time:str,email:str):
    return [day,time,email]

@app.post("/gpt")
async def chatGPT(prompt: str):
    info = """
    Name: CENTRE DENTAL CEREC, IMPLANT. LASER. COSMETIC & FAMILY DENTISTRY John Shi PC
    Bot Assistant Name: Natalie
    Insurance Accepted: All PPOs, claim Union plans, cannot accept Medicaid or DMOs. Generally out of network providers.
    New Patient Special: $150 for comprehensive exam, X-rays, iTero 5D scan, and regular cleaning. Request appointment to claim offer.
    Services Offered:
    - Root Canal
    - Dental Implants
    - Full Mouth Reconstruction
    - Teeth Whitening
    - Veneers
    - Invisalign
    - Wisdom Teeth
    - Pinhole Gum Rejuvenation
    - Teeth Cleaning
    - PRF Treatment
    - Digital Impression
    - Laser Dentistry
    - Laser Snore Therapy
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an assistant that helps patients about our clinic. Here is some information about our clinic:\n{info}"},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Okay, Understood. I can totally do that"},
            {"role": "user", "content": "num1 = 10\nnum2 = 5\nresult = num1 * num2\nprint('The result of multiplication is:', result)"}
        ]
    )

    # Handle the response as needed
    return response
