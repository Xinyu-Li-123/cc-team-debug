#!/usr/bin/env python3
import pickle

with open("results_ref.pkl", "rb") as file:
    results = pickle.load(file)

print(len(results))
print(results)
