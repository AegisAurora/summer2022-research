from src.ds import example, data
from src.utils import parse, parseMulti, removeCause
from src.runner import runner



def main():
    a = parse("./data/conjunctionNA")
    #a = parseMulti("./data/multi")
    experiments =a.makeAllExps(30)
    #experiments =a.makeTrials(10,5)
    #experiments = a.makeMultiExps(40)
    r = runner(path="./experiments-7-25/ConNa30",openAIKey="")
    r.setAI21Key("Bearer ")
    r.add(experiments)


    r.run(provider="AI21",model="j1-jumbo")
    #r.rumMulti()
    #r.runModels()
    #r.runTrials()




    #removeCause("./data/test")




if __name__ == "__main__":
    main()
