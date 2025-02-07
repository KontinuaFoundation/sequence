import numpy as np

# grams, diameter of a snail
data_mean = np.array([4.2, 2.3])

data_cov = np.array([[1.2, 0.45],[0.45, 0.5]])

n = 89

data = np.random.multivariate_normal(data_mean, data_cov, size=n)

print(f"data={data}")

with open("data.txt","w") as f:
    print("grams,cm", file=f)

    for i in range(len(data)):
        print(f"{data[i][0]},{data[i][1]}", file=f)
