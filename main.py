from crewai import Crew
from agents import ImageAgents
from tasks import ImageTasks
from dotenv import load_dotenv

load_dotenv()

def image_generation_crew(query):
    # Initialize components
    agents = ImageAgents()
    tasks = ImageTasks()
    
    # Create agents
    researcher = agents.researcher()
    writer = agents.writer()
    image_agent = agents.image_specialist()

    # Create tasks
    research_task = tasks.research_task(researcher, query)
    writing_task = tasks.writing_task(writer, query)
    image_task = tasks.image_generation_task(image_agent)

    # Assemble crew
    crew = Crew(
        agents=[researcher, writer, image_agent],
        tasks=[research_task, writing_task, image_task],
        verbose=True
    )

    # Execute workflow
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    user_query = input("Enter your image concept: ")
    result = image_generation_crew(user_query)
    print(f"Image generated at: {result}")