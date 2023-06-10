import streamlit as st
import streamlit.runtime.caching.cache_data_api
import torchvision
model = torchvision.models.resnet50(pretrained=True).eval()

import requests
from PIL import Image
from io import BytesIO

st.caption (f'getting image...')

# response = requests.get("https://unsplash.com/photos/ZxNKxnR32Ng/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8NHx8bGlvbnxlbnwwfHx8fDE2NzU3OTY5NjE&force=true")
response = requests.get("https://unsplash.com/photos/K_Na5gCmh38/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8Mnx8ZGVlcnxlbnwwfHx8fDE2ODYzMjAxMzh8MA&force=true")

image = Image.open(BytesIO(response.content))
st.image(image)

st.caption (f'importing transforms...')
from torchvision import transforms

def process_image(image):
    st.caption (f'processing image...')
    center_crop = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        ])
    normalize = transforms.Compose([
        # convert the image to a tensor with values between 0 and 1
        transforms.ToTensor(),
        # normalize to follow 0-centered imagenet pixel rgb distribution
        transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
        )
        ])
    return normalize(center_crop(image)).unsqueeze(0)

input_img = process_image(image)

import json

# /resources/imagenet_class_index.json
def load_data_labels(path: str =  './resources/imagenet_class_index.json'):
    st.caption(f'loading data lables...')
    # Opening JSON file
    st.caption(f'path = {path}')
    f = open(path)
    # returns JSON object as
    # a dicti
    data = json.load(f)
    return data

labels = load_data_labels()

import torch

def predict_classes(input_img, labels, model, total_preds: int = 5):
    st.caption(f'getting prediction...')
    # Find the score in terms of percentage by using torch.nn.functional.softmax function
    # which normalizes the output to range [0,1] and multiplying by 100
    out = model(input_img)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    # Find the index (tensor) corresponding to the maximum score in the out tensor.
    # Torch.max function can be used to find the information
    _, indices = torch.sort(out, descending=True)
    prediction = [(idx.item(), labels[str(idx.item())][1], percentage[idx].item()) for idx in indices[0][:total_preds]]

    return prediction

prediction = predict_classes(input_img, labels, model, 5)
st.write(f'prediction: {prediction}')

with st.expander(f'about models...'):
    st.caption("""
    You can find pre-trained PyTorch models in several places. Here are some common sources:

1. PyTorch Model Zoo: The official PyTorch website hosts the PyTorch Model Zoo, which contains a collection of pre-trained models for various tasks such as image classification, object detection, semantic segmentation, and more. You can find it at: https://pytorch.org/docs/stable/torchvision/models.html

2. torchvision.models: PyTorch's torchvision library provides a set of popular pre-trained models that can be used for computer vision tasks. You can find the list of models and their usage examples in the official PyTorch documentation: https://pytorch.org/vision/stable/models.html

3. Hugging Face Model Hub: The Hugging Face Model Hub (https://huggingface.co/models) is a popular platform for accessing pre-trained models for natural language processing (NLP) tasks. They provide a wide range of models, including state-of-the-art models like BERT, GPT, and RoBERTa, along with tutorials and code examples.

4. GitHub repositories: Many researchers and developers share their pre-trained PyTorch models on GitHub. You can search for specific models or projects related to your task of interest and explore their repositories. GitHub's search feature or platforms like GitHub Explore (https://github.com/explore) can help you discover relevant repositories.

When using pre-trained models, make sure to check the licensing terms and any specific requirements or instructions provided by the authors or organizations hosting the models.
""")


