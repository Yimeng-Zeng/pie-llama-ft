model=UtopiaLtd/pie-llama-7b
volume=$PWD/saved-models/ # share a volume with the Docker container to avoid downloading weights every run
max_best_of=100 # max number of samples to generate in parallel

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference:latest \
--model-id $model --max-best-of $max_best_of
