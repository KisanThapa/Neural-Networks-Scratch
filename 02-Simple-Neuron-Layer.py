# 2. Single layered 4 inputs and 3 outputs

mInputs = [3, 4, 1, 2]

mWeights1 = [0.2, -0.4, 0.6, 0.4]
mWeights2 = [0.4, 0.3, -0.1, 0.8]
mWeights3 = [0.7, 0.6, 0.3, -0.3]

mBias1 = 3
mBias2 = 4
mBias3 = 2

mOutputs = [mInputs[0]*mWeights1[0] + mInputs[1]*mWeights1[1] + mInputs[2]*mWeights1[2] + mInputs[3]*mWeights1[3] + mBias1,
            mInputs[0]*mWeights2[0] + mInputs[1]*mWeights2[1] + mInputs[2]*mWeights2[2] + mInputs[3]*mWeights2[3] + mBias2,
            mInputs[0]*mWeights3[0] + mInputs[1]*mWeights3[1] + mInputs[2]*mWeights3[2] + mInputs[3]*mWeights3[3] + mBias3]

print(mOutputs)
