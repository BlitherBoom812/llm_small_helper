export HF_ENDPOINT=https://hf-mirror.com
export HF_CACHE=$HF_DIR
export TRANSFORMERS_CACHE=$HF_DIR
export HUGGINGFACE_HUB_CACHE=$HF_DIR
export HF_HOME=$HF_DIR
ORGS=ToolBench
MODEL=ToolLLaMA-2-7b-v2
huggingface-cli download --resume-download --local-dir-use-symlinks False $ORGS/$MODEL --local-dir $HUGGINGFACE_HUB_CACHE/$MODEL
