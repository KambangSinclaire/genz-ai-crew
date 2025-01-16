#!/usr/bin/env python
from random import randint

from crewai.flow.flow import Flow, listen, start

from crews.content.content_creation import ContentCreationCrew
from dotenv import load_dotenv

load_dotenv()



class ContentCreationFlow(Flow):
    niche = ""
    topic = ""

    @start()
    def starting_crew(self):
        print("**** Starting the Content Creation Process *******")
        self.niche = input("What's your niche?\n")
        self.topic = input("What's the topic of today's video? \n")

    @listen(starting_crew)
    def generate_content_plan(self):
        result = (
            ContentCreationCrew()
            .crew()
            .kickoff(inputs={"niche": self.topic, "audience":"adults"})
        )
        return result.raw
    
    @listen(generate_content_plan)
    def write_content_from_plan(self, plan):
        print("**** Now in saver ****")
        with open(f"{self.niche}.md", "w") as readme_file:
            readme_file.write(plan)


def kickoff():
    content_creation_flow = ContentCreationFlow()
    content_creation_flow.kickoff()


def plot():
    content_creationCrew_flow = ContentCreationFlow()
    content_creationCrew_flow.plot()


if __name__ == "__main__":
    kickoff()