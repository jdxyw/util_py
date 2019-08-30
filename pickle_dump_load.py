import pickle

with open("temp.pkl", "wb") as f:
    pickle.dump([1,2,3], f)

with open("temp.pkl", "rb") as f:
    l = pickle.load(f)
    print(l)