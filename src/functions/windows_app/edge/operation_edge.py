from functions.windows_app.edge.edge_app import Edge
from settings import EDGE_PATH


app = Edge()

def start_edge():
    app.start_app(EDGE_PATH)