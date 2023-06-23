from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ChatForm
from .chatgpt import generate_response
from .models import Response
import json

# def chat(request):
#     if request.method == 'POST':
#         form = ChatForm(request.POST)
#         if form.is_valid():
#             user_input = form.cleaned_data['input']
#             response = generate_response(user_input)
#             return JsonResponse({'response': response})
#     else:
#         form = ChatForm()
#     return JsonResponse({'error': 'Invalid request'})

def home(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['input1']
            # prompt = f"""
            # \nI am doing research on skills and tools commonly required by various occupations.
            # My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada. Based on a given job title,
            # I want you to identify the most likely NOC code, then provide me with a list of the top skills and tools used on the job.
            # Please provide a response in JSON format, and only return the output for the NOC code you identify for the role of 
            # {user_input}. Include a node for "skills" and another for "tools".
            # """ 
            prompt = f"""
            \n Based on a given job title,
            I want you to identify the most likely NOC code, then provide me with a list of the top skills and tools used on the job.
            Please provide a output only  in JSON format with a node for "NOC_Title", node for "NOC" code you identify for the role of 
            {user_input}. Include a node for "required_Education", a node for "skills", a node for "Average_salary", and another for "tools".
            """ 
            response = generate_response(prompt)
            print (f"\nresponse from generate_response function :\n{response}")

            response_json = json.loads(response)

            response_dict = {
                "job_Title": response_json["NOC_Title"],
                "NOC": response_json["NOC"],
                "Education": response_json["required_Education"],
                "Salary": response_json["Average_salary"],
                "Skills": response_json["skills"],
                "Tools": response_json["tools"]
            }

            print(response_dict)
            
            str_response = json.dumps(response_dict)
            print(str_response)

            noc_code = response_json["NOC"]

            prompt2 = f"""I am doing research on transferable skills between similar occupations. My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada. Based on a given NOC code, I want you to identify 5 similar jobs with a percentage similarity estimate based on overlapping skills and education requirements.

            Please provide a response in JSON format only, based on the given NOC code. Include the original job title, and a node called "similar_jobs" with sub-nodes containing "job_title", "noc_code" and "percent_similarity".

            The NOC I need you to analyze is {noc_code}.
            
            """
            result = generate_response(prompt2)
            result_json = json.loads(result)

            result_dict = {
            "job_title": response_json["NOC_Title"],
            "similar_jobs": result_json["similar_jobs"],
            }



            return render(request, 'response.html', {'response': response_dict, 'result': result_dict})
            # return redirect('noc_result', response=response)
            # return redirect('response', response=response)


    else:
        form = ChatForm()

    context = {'form': form}
    return render(request, 'home.html', context)

def noc_Result(request, response):

    prompt = """
        I am doing research on skills and tools commonly required by various occupations.
        My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada.
        Based on NOC code, provide me with a list of similar jobs including the top skills and tools used on the job.
        Please provide a response in JSON format only, for the {response}.
        Include nodes for "title", "skills", and "tools".
        """
    result = generate_response(prompt)
    print(result)
    form = Response()
    context = {'form': form, 'response': response}  # Pass the 'response' object to the template context
    return render(request, 'Noc_Result.html', context)

def find_similiar_jobs(request, response):
    prompt = f"""
    I am doing research on transferable skills between similar occupations. My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada. Based on a given NOC code, I want you to identify 5 similar jobs with a percentage similarity estimate based on overlapping skills and education requirements.

    Please provide a response in JSON format only, based on the given NOC code. Include the original job title, and a node called "similar_jobs" with sub-nodes containing "job_title", "noc_code" and "percent_similarity".

    The NOC I need you to analyze is {response.NOC}.
    """
    result = generate_response(prompt)



# def noc_Result(request, response):
#     if request.method == 'POST':
#         prompt = """
#             I am doing research on skills and tools commonly required by various occupations.
#             My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada.
#             Based on NOC code, provide me with a list of similar jobs including the top skills and tools used on the job.
#             Please provide a response in JSON format only, for the {response}.
#             Include nodes for "title", "skills", and "tools".
#             """
#         result = generate_response(prompt)
#         print(result)
#         form = Response()
#         context = {'form': form, 'response': response}  # Pass the 'response' object to the template context
#         return render(request, 'Noc_Result.html', context)
#     else:
#         return HttpResponseServerError('Invalid request')


# def response_view(request, response):
#     context = {'response': response}
#     return render(request, 'response.html', context)




def response_view(request, response):
    # Parse the JSON response into a Python dictionary
    response_data = json.loads(response)

    # Extract the NOC, skills, and tools from the response data
    noc = response_data['NOC']
    skills = response_data['skills']
    tools = response_data['tools']

    # Prepare the context data to be passed to the template
    context = {
        'noc': noc,
        'skills': skills,
        'tools': tools,
    }

    return render(request, 'response.html', context)



