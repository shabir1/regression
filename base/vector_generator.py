from json import loads
from base.multiple_regression import MultipleRegression

base = '../data/'
train_vec_file = 'example-data-1.jl'
lines = [loads(line) for line in open(base + train_vec_file)]
count = 0
features = [
    "x1",
    "x2",
    "x3",
    "x4",
    "x5"
]

X_train = []
y_train = []
for line in lines:
    vector = []
    for f in features:
        v = line.get(f, 0.0)
        if str(v).strip() == '':
            vector.append(0.0)
        else:
            vector.append(v)
    y_train.append(line.get('y'))
    X_train.append(vector)


# Train Model
reg = MultipleRegression()
reg.evaluate(X_train, y_train, X_train, y_train)
