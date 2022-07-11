from src.ds import example, data
from src.parse import parse
from src.runner import runner



def main():
    a = parse("./data/Disjunctive-Syllogism")
    experiments =a.makeAllExps(5)
    r = runner(path="./test-exp",openAIKey="  ")
    r.setAI21Key("bearer ")
    r.add(experiments)
    r.run(provider="openAI",model="text-davinci-002")
    




if __name__ == "__main__":
    main()