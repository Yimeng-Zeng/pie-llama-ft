CUDA_VISIBLE_DEVICES="5,6" torchrun --nproc_per_node=2 \
    --master_port=1234 full_ft.py \
    --base_model "codellama/CodeLlama-7b-hf" \
    --data_path ./data/pctile/ \
    --output_dir saved-models/test_1 \
    --batch_size 64 \
    --micro_batch_size 1 \
    --num_epochs 1 \
    --learning_rate 1e-5 \
    --cutoff_len 1024 \
    --train_on_inputs False \
    --prompt_template_name "code_opt_w_speedup_pctile" \
    --use_flash_attention True \
    --train_name "pie_pctile_train.jsonl" \
    --val_name "pie_pctile_val.jsonl" \
    --with_pctile True \