from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ContentCreationCrew:
    """ContentCreation Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["content_creator"],
        )
    
    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_writer"],
        )


    @task
    def video_plan(self) -> Task:
        return Task(
            config=self.tasks_config["video_plan"],
        )
        
    @task
    def video_script(self) -> Task:
        return Task(
            config=self.tasks_config["video_script"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the content creation Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
