from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")

class ImageAgents:
    def researcher(self):
        return Agent(
            role='Market Research Analyst',
            goal='Research trending visual concepts and user preferences',
            backstory='Expert in analyzing current trends and user behavior patterns',
            verbose=True,
            llm=llm
        )

    def writer(self):
        return Agent(
            role='Creative Writer',
            goal='Generate compelling image descriptions and prompts',
            backstory='Skilled in creating vivid, detailed visual descriptions',
            verbose=True,
            llm=llm
        )

    def image_specialist(self):
        return Agent(
            role='Image Generation Expert',
            goal='Create high-quality images based on descriptions',
            backstory='Professional visual artist with technical image generation skills',
            verbose=True,
            llm=llm
        )