import numpy as np

class SGD(object):
    """
    Stochastic Gradient Descent (SGD)
    """

    def __init__(self,learning_rate = 0.01,momentum = 0,batch_size = 1):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.w_updt = None
        self.batch_size = float(batch_size)

    def update(self,w,grad_w):
        if self.w_updt is None:
            self.w_updt = np.zeros(np.shape(w))
        self.w_updt = self.momentum * self.w_updt + (1-self.momentum) * grad_w
        return w - self.learning_rate * (1/self.batch_size) * self.w_updt

class AdaGrad(object):
    """
    Adapative Gradient Descent by Duchi et al.
    """
    def __init__(self,learning_rate = 0.01,batch_size = 1):
        self.learning_rate = learning_rate
        self.cache = None
        self.batch_size = float(batch_size)

    def update(self,w,grad_w):
        epsilon = 1e-5
        if self.cache is None:
            self.cache = np.zeroes(np.shape(w))

        self.w_updt = grad_w/ (np.sqrt(self.cache) + epsilon)
        self.cache += np.square(grad_w)

        return w - self.learning_rate * (1/self.batch_size) * self.w_updt

class RMSProp(object):
    """
    Root Mean Square Propogation
    """

    def __init__(self,learning_rate = 0.01,momentum = 0,batch_size = 1):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.w_updt = None
        self.batch_size = float(batch_size)

    def update(self,w,grad_w):
        if self.w_updt is None:
            self.w_updt = np.zeros(np.shape(w))
        self.w_updt = self.momentum * self.w_updt + (1-self.momentum) * grad_w
        return w - self.learning_rate * (1/self.batch_size) * self.w_updt


