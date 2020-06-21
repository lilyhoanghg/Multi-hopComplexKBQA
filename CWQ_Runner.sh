python code/KBQA_Runner.py  \
        --train_folder  data/train_CWQ \
        --dev_folder data/dev_CWQ \
        --test_folder data/test_CWQ \
        --vocab_file data/CWQ/vocab.txt \
        --KB_file data/CWQ/kb_cache.json \
        --M2N_file data/CWQ/m2n_cache.json \
        --QUERY_file data/CWQ/query_cache.json \
        --output_dir trained_model/CWQ \
        --config config/bert_config.json \
        --gpu_id 1\
        --load_model trained_model/CWQ/Best \
        --save_model Best \
        --max_hop_num 3 \
        --num_train_epochs 30 \
        --do_train 0\
        --do_eval 1\
        --do_policy_gradient 1\
        --learning_rate 5e-5 \