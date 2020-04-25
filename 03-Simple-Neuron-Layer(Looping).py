# 3. Single layered 4 inputs and 3 outputs(Looping)

mInputs = [3, 4, 1, 2]

mWeights = [[0.2, -0.4, 0.6, 0.4],
            [0.4, 0.3, -0.1, 0.8],
            [0.7, 0.6, 0.3, -0.3]]

mBias1 = [3, 4, 2]

layer_output = []

for neuron_weights, neuron_bias in zip(mWeights, mBias1):
    neuron_output = 0
    for n_inputs, n_weights in zip(mInputs, neuron_weights):
        neuron_output += n_inputs*n_weights

    neuron_output += neuron_bias
    layer_output.append(neuron_output)


print(layer_output)
