from crewai import Task
from utils.image_generator import generate_image

class ImageTasks:
    def research_task(self, agent, query):
        return Task(
            description=f"""Research current visual trends related to: {query}
            Identify key elements, colors, and styles that are popular""",
            agent=agent,
            expected_output='Bullet-point report of visual trends and user preferences'
        )

    def writing_task(self, agent, query):
        return Task(
            description=f"""Create detailed image description based on research for: {query}
            Include style, composition, colors, and key elements""",
            agent=agent,
            expected_output='A 3-5 sentence vivid image description ready for generation'
        )

    def image_generation_task(self, agent):
        return Task(
            description="Generate the actual image using the provided description",
            agent=agent,
            expected_output='Saved image file path',
            action=lambda context: generate_image(context['previous_output'])
        )