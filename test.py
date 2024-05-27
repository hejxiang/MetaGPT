# main.py
import asyncio
from metagpt.roles.tutorial_assistant import TutorialAssistant

async def main(requirement: str):
   role = TutorialAssistant() 
   await role.run(requirement)

if __name__ == "__main__":
   requirement = "Redis教程"
   asyncio.run(main(requirement))