import openai
import json
from langgraph import Agent, LangGraph

# Configurer l'API OpenAI
openai.api_key = ''

# Classe de base pour l'agent
class BaseAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

# Agent pour identifier les objets dans une image
class Agent_Object_Identifier(BaseAgent):
    def __init__(self):
        super().__init__("Agent_Object_Identifier")
        
    def process(self, image_path):
        # Simulation de l'identification d'objets via ChatGPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that helps identify objects in images."},
                {"role": "user", "content": f"Please identify objects in the image at {image_path}"}
            ]
        )
        result = response['choices'][0]['message']['content']
        return json.loads(result)

# Agent pour classifier les objets identifiés
class Agent_Object_Classifier(BaseAgent):
    def __init__(self):
        super().__init__("Agent_Object_Classifier")
        
    def process(self, objects_json, classification_json):
        objects = json.loads(objects_json)
        classification = json.loads(classification_json)
        
        classified_objects = []
        for obj in objects:
            for class_type, keywords in classification.items():
                if any(keyword in obj['description'] for keyword in keywords):
                    obj['classification'] = class_type
                    break
            classified_objects.append(obj)
            
        return json.dumps(classified_objects, indent=2)

# Création de l'application LangGraph
class SmartSellApp:
    def __init__(self):
        self.graph = LangGraph("Smart Sell")
        self.agent_identifier = Agent_Object_Identifier()
        self.agent_classifier = Agent_Object_Classifier()
        
        self.graph.add_agent(self.agent_identifier)
        self.graph.add_agent(self.agent_classifier)
        
    def run(self, image_path, classification_json):
        objects_json = self.agent_identifier.process(image_path)
        classified_objects_json = self.agent_classifier.process(objects_json, classification_json)
        return classified_objects_json

# Exemple d'utilisation de l'application
if __name__ == "__main__":
    app = SmartSellApp()
    image_path = "./photo_slips.jpg"
    classification_json = json.dumps({
        "Electronics": ["phone", "laptop", "camera"],
        "Furniture": ["table", "chair", "sofa"]
    })
    result = app.run(image_path, classification_json)
    print("Classified Objects:", result)