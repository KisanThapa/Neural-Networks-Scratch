# 1. Single layered 4 inputs and 1 output neural network

inputs = [1, 3, 5, 2]

weights = [0.4, 0.6, -0.5, 0.2]

bias = 4

output = inputs[0]*weights[0] + inputs[1]*weights[1] + \
    inputs[2]*weights[2] + inputs[3]*weights[3] + bias

print(output)


# 2. Single layered 4 inputs and 3 outputs
mInputs = [3, 4, 1, 2]
mWeights = [[0.2, -0.4, 0.6],
            [0.4, 0.3, -0.1],
            [0.7, 0.6, 0.3],
            [0.4, 0.8, -0.3]]

mBias = [3, 4, 2]


mOutputs = [mInputs[0]*mWeights[0][0] + mInputs[1]*mWeights[1][0] + mInputs[2]*mWeights[2][0] + mInputs[3]*mWeights[3][0] + mBias[0],
            mInputs[0]*mWeights[0][1] + mInputs[1]*mWeights[1][1] +
            mInputs[2]*mWeights[2][1] + mInputs[3]*mWeights[3][1] + mBias[1],
            mInputs[0]*mWeights[0][2] + mInputs[1]*mWeights[1][2] + mInputs[2]*mWeights[2][2] + mInputs[3]*mWeights[3][2] + mBias[2]]

print(mOutputs)
