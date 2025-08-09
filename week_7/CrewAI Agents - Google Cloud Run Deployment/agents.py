from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os 

# Load environment variables
load_dotenv()  

# Get API key with validation
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in your environment or .env file.")

os.environ["GOOGLE_API_KEY"] = api_key

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=api_key  # Explicitly pass the API key
)

def research_agent(topic):
    """Simple research function"""
    
    # Create the research agent
    researcher = Agent(
        role='Researcher',
        goal='Research topics and provide useful information',
        backstory='You are a helpful researcher who finds good information about topics.',
        llm=llm
    )
    
    # Create the task
    task = Task(
        description=f"Research this topic: {topic}. Provide useful information and examples.",
        expected_output="A helpful report about the topic",
        agent=researcher
    )
    
    # Run the research
    crew = Crew(agents=[researcher], tasks=[task])
    result = crew.kickoff()
    
    return str(result)


def blog_team(topic):
    """Simple blog creation function"""
    
    # Create the agents
    researcher = Agent(
        role='Researcher',
        goal='Find information about topics',
        backstory='You research topics to help writers.',
        llm=llm
    )
    
    writer = Agent(
        role='Writer',
        goal='Write good blog posts',
        backstory='You write clear and interesting blog posts.',
        llm=llm
    )
    
    editor = Agent(
        role='Editor',
        goal='Make writing better',
        backstory='You fix grammar and make writing clearer.',
        llm=llm
    )
    
    # Create the tasks
    research_task = Task(
        description=f"Research information about: {topic}",
        expected_output="Research findings",
        agent=researcher
    )
    
    write_task = Task(
        description=f"Write a blog post about: {topic}",
        expected_output="A blog post",
        agent=writer
    )
    
    edit_task = Task(
        description="Edit the blog post to make it better",
        expected_output="Final blog post",
        agent=editor
    )
    
    # Run the team
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, write_task, edit_task]
    )
    
    result = crew.kickoff()
    return str(result)


