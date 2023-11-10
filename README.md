# pie-llama-ft
Repository for finetuning codellama models for the paper Learning Performance Improving Code Edits

train and validation data for performance conditioned experiments [can be found here](https://www.dropbox.com/scl/fo/md2tiewekc9vmbemgpqzd/h?rlkey=hryawwntfhbuhzram7jz8q4vu&dl=0)

## Environment setup

We provide a dockerfile in the ```/docker/``` directory, which should be sufficient to run our code

## training

We provide a training script for the performance conditioned code optimization task in ```train.sh```

## Sampling

We have uploaded the [7b](https://huggingface.co/UtopiaLtd/pie-llama-7b) and [13b](https://huggingface.co/UtopiaLtd/pie-llama-13b) performance conditioned models to huggingface, to produce samples for our given test set of programs, first run ```server.sh```, and running the below code will produce 8 samples for each program at a temperature of 0.7.

```bash
python sample.py --test_file eval/data/cleaned_test_results.jsonl --output_file eval/results.jsonl --do_sample True --num_threads 8 --temperature 0.7 --num_samples 8 --prompt_name code_opt_w_speedup_pctile_test
```


