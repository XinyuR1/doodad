CODE_DIRS_TO_MOUNT = [
    ## location of SMiRL code
]
NON_CODE_DIRS_TO_MOUNT = [
    ## Maybe some simulation you are importing to run.
]
LOCAL_LOG_DIR = '/tmp/doodad-output/'
OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/'
DIR_AND_MOUNT_POINT_MAPPINGS = [
    dict(
        local_dir='/home/gberseth/.mujoco/',
        mount_point='/root/.mujoco',
    ),
#     dict(
#         local_dir='/home/gberseth/playground/CoMPS',
#         mount_point='/root/playground/CoMPS',
#     ),
#     dict(
#         local_dir='/home/gberseth/playground/doodad_vitchry',
#         mount_point='/root/playground/doodad',
#     ),
]


"""
AWS Settings
"""
AWS_S3_PATH = 'TODO'

# The docker image is looked up on dockerhub.com.
DOODAD_DOCKER_IMAGE = 'TODO'
INSTANCE_TYPE = 'c4.2xlarge'
SPOT_PRICE = 0.3

GPU_DOODAD_DOCKER_IMAGE = 'TODO'
GPU_INSTANCE_TYPE = 'g3.4xlarge'
GPU_SPOT_PRICE = 0.5
REGION_TO_GPU_AWS_IMAGE_ID = {
    'us-west-1': "ami-874378e7",
    'us-east-1': "ami-ce73adb1",
}
AWS_FILE_TYPES_TO_SAVE = (
    '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
    '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
    '*.jpeg', '*.patch', '*.html'
)

"""
SSH Settings
"""
SSH_HOSTS = dict(
    default=dict(
        username='TODO',
        hostname='TODO.domain.edu',
    ),
)
SSH_DEFAULT_HOST = 'user'
SSH_PRIVATE_KEY = '~/.ssh/id_rsa'
SSH_LOG_DIR = '~/shared/res'
SSH_TMP_DIR = '~/shared/tmp'

"""
Local Singularity Settings
"""
SINGULARITY_IMAGE = 'TODO'
SINGULARITY_PRE_CMDS = [
]


"""
BRC/Slurm Settings

These are basically the same settings as above, but for the remote machine
where you will be running the generated script.
"""
SLURM_CONFIGS = dict(
    cpu=dict(
        account_name='TODO',
        partition='TODO',
        n_gpus=0,
        max_num_cores_per_node=20,
    ),
    gpu=dict(
        account_name='TODO',
        partition='TODO',
        n_gpus=1,
        max_num_cores_per_node=8,
        n_cpus_per_task=2,
    ),
)
BRC_EXTRA_SINGULARITY_ARGS = '--writable -B /usr/lib64 -B /var/lib/dcv-gl'
TASKFILE_PATH_ON_BRC = 'TODO'


SSS_CODE_DIRS_TO_MOUNT = [
]
SSS_NON_CODE_DIRS_TO_MOUNT = [
]
SSS_LOG_DIR = '/global/scratch/user/doodad-log'


SSS_GPU_IMAGE = 'TODO'
SSS_CPU_IMAGE = 'TODO'
SSS_RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = 'TODO'
SSS_PRE_CMDS = [
    'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH'
]


"""
GCP Settings

To see what zones support GPU, go to https://cloud.google.com/compute/docs/gpus/
"""
GCP_IMAGE_NAME = 'TODO'
GCP_GPU_IMAGE_NAME = 'TODO'
GCP_BUCKET_NAME = 'TODO'

GCP_DEFAULT_KWARGS = dict(
    zone='us-west1-a',
    instance_type='n1-standard-4',
    image_project='TODO',
    terminate=True,
    preemptible=False,  # is much more expensive!
    gpu_kwargs=dict(
        gpu_model='nvidia-tesla-k80',
        num_gpu=1,
    )
)
GCP_FILE_TYPES_TO_SAVE = (
    '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
    '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
    '*.jpeg', '*.patch', '*.html'
)

# Overwrite with private configurations

try:
    from launchers.config import *
    print ("Running Something?")
except:
    print ("Something not installed")
    pass 
