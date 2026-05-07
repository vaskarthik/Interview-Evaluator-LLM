from src.langchain.prompts import evaluation_prompt
from src.langchain.llm import llm
from src.langchain.output_parser import parser

evaluation_chain = evaluation_prompt | llm | parser