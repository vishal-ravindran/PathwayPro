from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ChatForm
from .chatgpt import generate_response
from .models import Response

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
            prompt = f"""
            \nI am doing research on skills and tools commonly required by various occupations.
            My primary reference is the National Occupation Classification (NOC) developed by the Government of Canada. Based on a given job title,
            I want you to identify the most likely NOC code, then provide me with a list of the top skills and tools used on the job.
            Please provide a response in JSON format only, for the NOC code you identify for the role of 
            {user_input.strip()}. Include a node for "skills" and another for "tools".
            """ 

            response = generate_response(prompt)
            print(response)
            # return redirect('noc_result', response=response)
            return redirect('response', response=response)


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


def response_view(request, response):
    context = {'response': response}
    return render(request, 'response.html', context)


