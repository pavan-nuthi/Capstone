# MVSAT

## Requirements
You can install the conda environment by running:
```bash
conda create -n a2summ python=3.8.13
conda activate a2summ
pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
pip install tensorboard
pip install rouge-score==0.1.2
pip install scipy ortools h5py pyyaml
```

## Running

### Training
We train the model on a single GTX-1080ti GPU. To train the model on different dataset, please execute the following command.
```bash
python train.py --dataset ${dataset}
```

### Testing
First, download the [checkpoints](https://drive.google.com/file/d/1LuXWjW3BcAXCOals4o2UUVYMx-FYnJ3T/view?usp=sharing) into "saved_model" directory and pass it as the checkpoint flag. 

```bash
python train.py --dataset ${dataset} \
    --test --checkpoint saved_model/${dataset}
```
