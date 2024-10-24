# gamedev-copilot

### To run:

1. Go to https://www.paperspace.com/ & login
2. Create core machine (anything high GPU)
   1. create private network & add an IP as needed
3. SSH into the server
4. `docker run --gpus '"all"' --rm -it winglian/axolotl:main-latest`
5. Open VS Code into the server and into the docker container (make sure you have remote-ssh and docker extensions on VS Code)
6. inside the docker container, run:
7. `git clone https://<access token>@github.com/RiccLQL/gamedev-copilot.git`
8. `wandb login --relogin`
9. `huggingface-cli login`
10. `CUDA_VISIBLE_DEVICES="" python -m axolotl.cli.preprocess <path to .yml>`
11. `accelerate launch -m axolotl.cli.train <path to .yml>`