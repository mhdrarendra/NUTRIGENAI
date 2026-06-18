import google.generativeai as genai
from PIL import Image
import json
import os
from dotenv import load_dotenv
import streamlit as st

# 🔥 LANGSUNG TARUH API KEY DI SINI
GEN_AI_API = os.getenv("GEN_AI_API")
print(GEN_AI_API)
genai.configure(api_key=GEN_AI_API)