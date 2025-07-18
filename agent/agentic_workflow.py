from utils_model_loader import utils_model_loader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prbuild import ToolNode, tools_condition




class GraphBuilder(object):
    def __init__(self, graph):
        self.graph = graph

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, from_node, to_node):
        self.graph.add_edge(from_node, to_node)

    def get_graph(self):
        return self.graph