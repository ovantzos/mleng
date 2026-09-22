# ML Engineering Workbench

|Project|Paper|Implementation|Engineering Skills|
|-------|-----|--------------|------------------|
|1. CNNs|[Deep Residual Learning for Image Recognition — He et al., 2015](https://arxiv.org/abs/1512.03385)|Residual blocks, normalization, training loop|PyTorch fundamentals, optimization|
|2. Vision Transformers| [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale — Dosovitskiy et al., 2020](https://arxiv.org/abs/2010.11929)| Patch embedding, attention, positional embeddings| Transformer internals|
|3. Generative Models| [Auto-Encoding Variational Bayes — Kingma & Welling, 2013](https://arxiv.org/abs/1312.6114)| Encoder/decoder, reparameterization, ELBO| Generative modeling|
|4. GANs| [Unsupervised Representation Learning with Deep Convolutional GANs — Radford et al., 2015](https://arxiv.org/abs/1511.06434)| Generator/discriminator, adversarial training| Training instability|
|5. Neural Rendering| [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis — Mildenhall et al., 2020](https://arxiv.org/abs/2003.08934)| Ray sampling, positional encoding, volume rendering| Differentiable rendering|
|6. Diffusion| [Denoising Diffusion Probabilistic Models — Ho et al., 2020](https://arxiv.org/abs/2006.11239)| Forward process, noise prediction, reverse sampling| Modern image generation|
|7. Latent Diffusion| [High-Resolution Image Synthesis with Latent Diffusion Models — Rombach et al., 2021](https://arxiv.org/abs/2112.10752)| VAE + U-Net + cross-attention + diffusion| End-to-end generative systems|
|8. Modern U-Nets| [Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet) — Zhang et al., 2023](2302.05543)| Conditioning branch + zero convolutions| Conditional generation| 
|9. 3D generation| [DreamFusion: Text-to-3D using 2D Diffusion — Poole et al., 2022](https://arxiv.org/abs/2209.14988)| Score distillation + differentiable rendering| 2D→3D optimization|
|10. Video Generation| [Video Diffusion Models — Ho et al., 2022](https://arxiv.org/abs/2204.03458)| Temporal attention / 3D U-Net| Spatiotemporal modeling|
|11. Modern Video| [Scalable Diffusion Models with Transformers — Peebles & Xie, 2023](https://arxiv.org/abs/2308.09257)| Transformer-based diffusion| Scaling architectures|
|12. Gaussian Splats| [3D Gaussian Splatting for Real-Time Radiance Field Rendering — Kerbl et al., 2023](https://arxiv.org/abs/2308.04079)| Gaussian representation + differentiable rasterization| Graphics + CUDA-oriented engineering|
