Minimal Wasserstein GAN
=======================

This is a simple TensorFlow implementation of Wasserstein Generative Advesarial Networks applied to MNIST.

Some example generated digits:

![WGAN results](https://user-images.githubusercontent.com/2202312/32365134-e8a7d78e-c078-11e7-91c6-82cf9a11e7ea.png)


How to run
----------

Simply run the file [`wgan_mnist.py`](wgan_mnist.py). Results will be displayed in real time, while full training takes about an hour using a GPU.

Implementation details
----------------------

The implementation follows [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028), using the network from [the accompanying code](https://github.com/igul222/improved_wgan_training). In particular both the generator and discriminator uses 3 convolutional layers with 5x5 convolutions.
