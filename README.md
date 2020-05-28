# 4th place [Finnet Challenge](https://github.com/finnethackaton/finnet) solution

## Task description
  An anonymized graph of transactions between legal entities in Russia is given. Some of the edges were removed from it. The task is to restore them.
## Data description
Link to the dataset: https://drive.google.com/open?id=1dRfIzUsmwD-ZmURbwPbGjbG-kfcgDsd-

**vertices.csv** contain information about each company:
- id - id of a legal entity
- main_okved - main OKVED of the legal entity
- region_code - region code of the legal entity
- company_type - type of the legal entity

**edges.csv** contain information about transactions between companies:
- id_1 - first company id
- id_2 - second company id
- value - anonymized summary value of all transactions
- n_transactions - anonymized number of transactions between id_1 and id_2

**ids.csv** contain ids we have to predict edges for
- id - id of the company

## Solution description
  My top 4 solution is just Node2Vec(walklen=4, dimensions=100) and a lot of different data mixed in one ensemble (9 CatBoost models).The most important things in my models were squared matrix of interactions each main_okved to each main_okved and the same case for region_code. I tried a lot of things including common NN with different ids embeddings, but it was absolutely bad for the public leaderboard. Also I tried to predict number of real edges, but it often predict value that less than real value, so it is useless.
## Notes
  During this competition I found wonderful python module to speedup Node2Vec computation which is based on CSR sparse matrices: [nodevectors](https://github.com/VHRanger/nodevectors)
## Additional data
- [Pretrained Node2Vec model](https://drive.google.com/open?id=1GHPqj_5pi3pPiRYuZvvtXhRKv38aVRhY)
- [Result of the work of each model from solution.ipynb](https://drive.google.com/open?id=1pErKYHUtORbRffrPhJhGtNeL9ck42Fge)
