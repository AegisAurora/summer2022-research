import openai
import requests

class runner():
    experiments = []
    path = ""
    openAIKey = ""
    AI21Key = ""
    models = {
        "openai":[],
        "ai21":[]
    }
    
    def __init__(self,experiments=[],path="./",openAIKey ="", AI21Key = ""):
        self.experiments = experiments
        self.path = path
        self.openAIKey = openAIKey
        self.AI21Key = AI21Key
    
    def add(self,*args):
        for i in args:
            self.experiments.append(i)

    def setOpenAIKey(self,key):
        self.openAIKey = key
    
    def setAI21Key(self,key):
        self.AI21Key = key
    
    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path
    
    def runOpenAI(self,model,experiment):
        assert self.openAIKey != "", "Please add OpenAI key with setOpenAIKey method"
        openai.api_key= self.openAIKey
        out=openai.Completion.create(engine=model, temperature=0, prompt=experiment, max_tokens=1024, stop="\n")
        out = out["choices"][0]["text"] + "\n"
        return out

    
    def runAI21(self,model,experiment):
        assert self.AI21Key != "", "Please add AI21 key with setAI21Key method"
        out = requests.post(
            f"https://api.ai21.com/studio/v1/{model}/complete",
            headers={"Authorization": self.AI21Key},
            json={
                "prompt": experiment, 
                "numResults": 1, 
                "maxTokens": 1024, 
                "stopSequences": ["\n"],
                "topKReturn": 0,
                "temperature": 0.0
            }    
        )
        out = out.json()["completions"][0]["data"]["text"] +"\n"
        return out
        

    def run(self,provider,model):
        assert provider == "openAI" or provider == "AI21", "Provider has to be openAI or AI21"
        n = 1
        for experiment in self.experiments[0]:
            a = f"----------------------------------EXPERIMENT NUMBER {n}--------------MODEL {model}--------------------\n"
            with open(self.path,"a") as f:
                f.write(a)
                f.write(experiment)
                if provider == "openAI":
                    f.write(self.runOpenAI(model,experiment))
                else:
                    f.write(self.runAI21(model,experiment))
            n += 1
