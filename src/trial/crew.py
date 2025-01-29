import os
from dotenv import load_dotenv
from langtrace_python_sdk import langtrace
load_dotenv()

langtrace.init(api_key = os.environ["LANGTRACE_API_KEY"])

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

search_tool = SerperDevTool()

@CrewBase
class Trial():
	"""Trial crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff
	def before_kickoff_function(self, inputs):
		print(f"Before kickoff function with inputs: {inputs}")
		return inputs # You can return the inputs or modify them as needed

	@after_kickoff
	def after_kickoff_function(self, result):
		print(f"After kickoff function with result: {result}")
		return result # You can return the result or modify it as needed


	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	# @agent
	# def researcher(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['researcher'],
	# 		verbose=True,
	# 		tools=[search_tool]
	# 	)
	
	# @agent
	# def business_researcher(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['business_researcher'],
	# 		verbose=True,
	# 		tools=[search_tool]
	# 	)

	# @agent
	# def wiki_article_writer(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['wiki_article_writer'],
	# 		verbose=True
	# 	)

	@agent
	def introduction_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['introduction_agent'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def data_and_facts_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_and_facts_agent'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def government_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['government_agent'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def economy_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['economy_agent'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def business_environment_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['business_environment_agent'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def infrastructure_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['infrastructure_agent'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def technology_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['technology_agent'],
			verbose=True,
			tools=[search_tool]
		)
	
	@agent
	def final_writer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['final_writer_agent'],
			verbose=True
		)
	
	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	# @task
	# def research_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['research_task'],
	# 		tools=[search_tool],
	# 		verbose=True
	# 	)
	
	# @task
	# def business_research_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['business_research_task'],
	# 		tools=[search_tool],
	# 		output_file='outputs/business_research.txt',
	# 		verbose=True
	# 	)

	# @task
	# def wiki_article_writing_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['wiki_article_writing_task'],
	# 		output_file='outputs/wiki_article.md',
	# 		verbose=True
	# 	)

	@task
	def introduction_task(self) -> Task:
		return Task(
			config=self.tasks_config['introduction_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/01introduction.md',
			verbose=True
		)

	@task
	def data_and_facts_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_and_facts_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/02data_and_facts.md',
			verbose=True
		)

	@task
	def government_task(self) -> Task:
		return Task(
			config=self.tasks_config['government_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/03government.md',
			verbose=True
		)

	@task
	def economy_task(self) -> Task:
		return Task(
			config=self.tasks_config['economy_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/04economy.md',
			verbose=True
		)

	@task
	def business_environment_task(self) -> Task:
		return Task(
			config=self.tasks_config['business_environment_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/05business_environment.md',
			verbose=True
		)

	@task
	def infrastructure_task(self) -> Task:
		return Task(
			config=self.tasks_config['infrastructure_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/06infrastructure.md',
			verbose=True
		)

	@task
	def technology_task(self) -> Task:
		return Task(
			config=self.tasks_config['technology_task'],
			tools=[search_tool],
			output_file='outputs/SanFrancisco/07technology.md',
			verbose=True
		)

	@task
	def final_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['final_writer_task'],
			output_file='outputs/SanFrancisco/00wiki_article.md',
			verbose=True
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Trial crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
