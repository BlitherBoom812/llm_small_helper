export HF_ENDPOINT=https://hf-mirror.com
ORGS=bigscience
MODEL=bloom-560m
huggingface-cli download --resume-download --local-dir-use-symlinks False $ORGS/$MODEL --local-dir /data_new/private/tianshizuo/$MODEL