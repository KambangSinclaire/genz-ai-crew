#!/usr/bin/env python
from random import randint

from crewai.flow.flow import Flow, listen, start

from crews.content.content_creation import ContentCreationCrew
from dotenv import load_dotenv

load_dotenv()



class ContentCreationFlow(Flow):
    input_str = ""

    @start()
    def starting_crew(self):
        print("**** Starting the Content Creation Process *******")
        input_st = input("What's your niche?")
        self.input_str = input_st

    @listen(starting_crew)
    def generate_content_plan(self):
        result = (
            ContentCreationCrew()
            .crew()
            .kickoff(inputs={"niche": self.input_str, "audience":"adults"})
        )
        print(result.raw)
        return result.raw
    
    # @listen(generate_content_plan)
    # def write_content_from_plan(self, plan):
    #     print("**** Now in writer ****")
    #     result = (Content)


def kickoff():
    content_creation_flow = ContentCreationFlow()
    content_creation_flow.kickoff()


def plot():
    content_creationCrew_flow = ContentCreationFlow()
    content_creationCrew_flow.plot()


if __name__ == "__main__":
    kickoff()