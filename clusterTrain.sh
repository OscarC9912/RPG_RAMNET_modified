#!/bin/bash
#SBATCH --job-name=rpg_train
#SBATCH --chdir=/h/sankeert/zhonghan_chen/RPG_RAMNET_modified
#SBATCH --open-mode=append
#SBATCH --output=/h/sankeert/zhonghan_chen/RPG_RAMNET_modified/slurm_output/logs/%x-%j.log
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=16G
#SBATCH --partition=t4v2
#SBATCH --qos=high
#SBATCH --gpus-per-task=1

export PREPROCESSED_DATASETS_FOLDER=/SCRATCH/project/data/training
CUDA_VISIBLE_DEVICES=0 python3 train.py --config configs/train_e2depth_si_grad_loss_statenet_ergb.json
