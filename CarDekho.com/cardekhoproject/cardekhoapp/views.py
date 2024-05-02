from django.shortcuts import render , reverse
from google.generativeai.types.generation_types import StopCandidateException
from django.http import HttpResponse ,  HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
import uuid
import time
from .models import *
import random
from django.db.models import Max
from django.contrib.sessions.backends.base import SessionBase
import google.generativeai as genai
# Create your views here.

def cardekho(request):
    return render(request, 'index.html')

def chat(request):
    chats = ChatConversation.objects
    return render(request, "index.html", {"chat": chats})

userm = ""
botm = ""
def ask_question(request):
    global user_message
    global bot_message
    if request.method == 'POST':
        """session_id = request.GET.get('session-id')
        sid = list(ChatConversation.objects.values_list('session_id',flat=True))
        if session_id in sid:
        # Check if 'usermessages' key exists in the session
            if 'usermessages' in request.session:
                user_messages = request.session['usermessages']
            # Check if 'usermessages' list is not empty
                if user_messages:
                    user_message = user_messages[-1]
                    bot_message = ChatConversation.objects.filter(session_id=session_id).last().bot_message
                    print("Bot Message:- ", bot_message, "\n", "User Message:- ", user_message)
                else:
                # Handle the case when 'usermessages' list is empty
                    print("No user messages in session")
            else:
            # Handle the case when 'usermessages' key is not present in the session
                print("No 'usermessages' key in session")
        else:
        # Handle the case when session_id is not found in sid list
            print("Session ID not found")"""
    
        try:
            #sid = generate_unique_chat_id()
            genai.configure(api_key="AIzaSyA4upAICdw0FU2MZHOcteFib0hrxrzDimw")
            generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

            safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

           
            model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                               safety_settings=safety_settings
                              )
            
            """if request.session['usermessages'][-1]:
                userm = request.session['usermessages'][-1]
            if request.session['botmessages'][-1]:
                botm = request.session['botmessages'][-1]"""
            #userme = request.POST.get('text')
            #otme = bot_message
            
            chat = model.start_chat(history=[
 {
    "role": "user",
    "parts": ["Hey, You are Ankit with 8 years of Experience of Customer Support Assistant , Automotive Industry of India and Sales. Say to user \"\\You can call me Ankit\". You are working for the CarDekho is an Indian online platform that caters to the needs of both car buyers and sellers. It provides a comprehensive range of services related to buying and selling new and used cars, making the car buying and selling journey smoother and more informed. https://www.cardekho.com/ . \n\nServices Offered by CarDekho:\nBuying and Selling Cars: CarDekho offers a platform for users to buy and sell new and used cars. They have a vast database of listings, allowing users to search for cars based on various criteria like brand, model, price, features, and fuel type.\nEMI Calculator: CarDekho provides an EMI calculator tool that helps users estimate their monthly car loan payments. This helps with budgeting and making informed financial decisions when purchasing a car.\nInsurance Options: CarDekho offers car insurance options through partnerships with various insurance providers. Users can compare plans and choose the one that best suits their needs and budget.\nAdvice on Selling Cars: CarDekho offers valuable advice on selling cars, including tips on preparing the car for sale, setting the right price, and negotiating with potential buyers.\nCar Valuation: CarDekho allows users to value their car through their online tool. This provides an estimated market value based on factors like the car's make, model, year, condition, and mileage.\nPopular Car Comparisons on CarDekho:\n\nThe website frequently features comparisons of popular car models, providing users with insights into different options available in the market. Some popular comparisons include:\n\nMaruti Suzuki Swift vs. Hyundai Creta\nTata Nexon vs. Kia Seltos\nCar Reviews:\n\nCarDekho also features reviews of recently released cars, offering users a comprehensive overview of the car's performance, features, and overall driving experience. This helps potential buyers make informed decisions before purchasing.\n\nKey Points about Featured Cars:\n\nMaruti Suzuki Swift: A popular hatchback known for its fuel efficiency. The new Swift boasts a sharper exterior design and major feature updates like a larger touchscreen infotainment unit. Bookings for the new generation model are now open.\nHyundai Creta: A popular SUV in India, available in various models with a starting price of Rs. 11 lakh. It offers features like a larger touchscreen infotainment unit.\nTata Nexon: A popular SUV and one of the safest hatchbacks in India with a 5-Star Global NCAP rating. It comes in electric and petrol variants. The electric variant offers a range of 4500km with prices starting at Rs 8.15 lakh. Key features include a spacious boot, a refined engine, and improved driveability. However, the mileage of the petrol variant has been noted as a weak point.\nKia Seltos: Another popular SUV, CarDekho offers a first-drive review discussing the car's performance during a road trip.\nTata Punch EV: An affordable electric vehicle with a range of 35 kwh and a starting price of Rs 7.99 lakh, making it one of the most budget-friendly EVs in India.\nBYD Seal: An electric sedan priced under Rs 60 lakh, potentially offering a competitive option in the luxury sedan market.\nAdditional Information:\n\nWhile the exact information about the founding company of CarDekho and its valuation is unavailable from the provided webpage, it's evident that CarDekho has established itself as a leading platform in the Indian car buying and selling market. Their diverse range of services and informative content cater to various user needs, making the car buying and selling process more streamlined and informed.\n\nSocial Media Accounts of CarDekho :-\nInstagram :- https://www.instagram.com/cardekhoindia/\nFacebook :- https://www.facebook.com/CarDekho/\nYoutube :- https://www.youtube.com/channel/UCMSjsvDuobchFSw5U1SDaqg\nLinkedin :- https://www.linkedin.com/company/cardekhogroup/\nX ( Twitter ):- https://twitter.com/CarDekho\n\nSo, Here is your tasks given below understand it carefully and worked on it :-\n1) Your first task is to collect user'name and their email id until user can't provide their name and mail id don't move forward , after collecting the user name and mail id welcome the user by their name {user'name}.\n2) You should suggest to user the used car's ( Extract the details of the car from the website ) according to the user needs. Ask user about their budget, car type , location, profession to provide them best car according to their needs ,requirements and their budget.\nYou suggest the car's also including the resale value of the car and current Situation of the Automotive Industry India.\n3) Solve the uesr quer if they are technical or fundamental or basic questions.\n4) Also tell the user about the EMI , Calculate the EMI according to their budget, give them advice from asking some question such as income , budget. ( Say to user \" The all things about EMI are not 100% accurate you should once go through them provide the link of the EMI page \"). help them to select best EMI Plan and guide them how they can afford this car. \n5) If the user come to sell their car then tell them the steps to sell the at best price and also tell them current market trends , market price of the car they want to sell. \n6) if the user want to do complaint about car fraud or car details are wrong then help them by getting the proper knowledge of their problem understand it and suggest them best way.\n7) Now, in the end if user queries end then thanks the user.\n8) Always talk with user like bestfriend but in Professional way. You can use emojis for attractiveness conservation"]
  },
  {
    "role": "model",
    "parts": ["## Hello there! You can call me Ankit! 👋\n\nI'm here to assist you with all your car buying and selling needs at CarDekho.  Before we begin, could you please share your name and email address? This will help me personalize your experience and keep you updated."]
  },



  
])
            #book = ('mail','Mail','Email','email','e-mail','book','booked','schedule','meeting','meeting','IST')
            question = request.POST.get('text')
            #userm = question
            response = chat.send_message(question)
            """if random.choice(book) in response:
                email = re.search(r'[\w\.-]+@[\w\.-]+', text).group()
                print(email)"""
              

            #schedule = ('otp','OTP')
            try :
                response_data = {
                "text": response.text
            } 

            

            
            except ValueError:
                response_data = {
                "text": response.prompt_feedback,
                "text": response.candidates[0].finish_reason,

                }
            #response = markdown.markdown(response)
            #botm = response_data['text']
            if 'usermessages' and 'botmessages' not in request.session:
                request.session['usermessages']= []
                request.session['botmessages'] = []
        
            
            user_message = question
            if user_message:
                usermess = user_message
                request.session['usermessages'].append(usermess)
                #print("User Message:- ",user_message)
                bot_messages = response.text
                request.session['botmessages'].append(bot_messages)
            usermessages = request.session['usermessages'][-1:]      
            botmessages = request.session['botmessages'][-1:]      

            print("Bot message:- ",chat)
            sid = generate_unique_chat_id()
            ChatConversation.objects.create(session_id=sid,bot_message=question, user_message=response.text).save()
            content = {
                "user": usermessages,
                "bot": botmessages
            }
            
            return JsonResponse({"messages": content})
        except StopCandidateException as e:
            print(f"StopCandidateException raised: {e}")
            return JsonResponse({"error": "An error occurred while processing your request."}, status=500)
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )



def generate_unique_chat_id():
    timestamp = int(time.time() * 100)  # Convert current timestamp to milliseconds
    random_num = random.randint(10000, 99999)  # Generate a random 5-digit number
    random_sub = random.randint(10,100)
    unique_id = int(str(timestamp) + str(random_num))  - int(random_sub)  # Combine timestamp and random number

    return unique_id


def newsletters(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        newsletter.objects.create(name=name,email=email).save()
        context = {"message":f"{name} You have successfully subscribed to our newsletter! Thank you for subscribing."}
        return render(request,'index.html',context)