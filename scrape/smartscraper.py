from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

graph_config = {
   "llm": {
      "model": "ollama/mistral",
      "temperature": 1,
      "format": "json",  # Ollama needs the format to be specified explicitly
      "model_tokens": 2000, #  depending on the model set context length
      "base_url": "http://localhost:11434",  # set ollama URL of the local host (YOU CAN CHANGE IT, if you have a different endpoint
   },
   "embeddings": {
      "model": "ollama/nomic-embed-text",
      "temperature": 0,
      "base_url": "http://localhost:11434",  # set ollama URL
   }
}

## graph instance run

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the links to github repos",
    source="https://github.com/leereilly/games",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)