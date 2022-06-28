#!/bin/bash
#alias python=python3
export PREPROCESSED_DATASETS_FOLDER=/SCRATCH/project/data/training
CUDA_VISIBLE_DEVICES=0 python3 train.py --config configs/train_e2depth_si_grad_loss_statenet_ergb.json