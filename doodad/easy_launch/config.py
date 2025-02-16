# Base Directory
"""
TODO: change BASE_CODE_DIR
"""
BASE_CODE_DIR = "/home/liuronni/Documents/Github"

# Mounting Directories for doodad
CODE_DIRS_TO_MOUNT = [
    BASE_CODE_DIR + "/rlkit"
]
NON_CODE_DIRS_TO_MOUNT = [
]

# Log Directories for doodad (locally)
"""
TODO: change the directories where you want to store your data
"""
LOCAL_LOG_DIR = BASE_CODE_DIR + "/rlkit/data"
OUTPUT_DIR_FOR_DOODAD_TARGET = BASE_CODE_DIR + "/rlkit/data"

DIR_AND_MOUNT_POINT_MAPPINGS = [
]

"""
AWS Settings
"""
AWS_S3_PATH = 'TODO'

# The docker image is looked up on dockerhub.com.
DOODAD_DOCKER_IMAGE = 'xinyur1/rlkit:version-cpu'
INSTANCE_TYPE = 'c4.2xlarge'
SPOT_PRICE = 0.3

GPU_DOODAD_DOCKER_IMAGE = 'xinyur1/rlkit:version-gpu3'
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
"""
TODO: change the usernames and the hostnames depending on which
servers you are using.
"""
SSH_HOSTS = dict(
    arcade=dict(
        username='liuronni',
        hostname='arcade'
    ),
    blue=dict(
        username='ronnie',
        hostname='blue'
    ),
    green=dict(
        username='ronnie',
        hostname='green'
    )
)
SSH_DEFAULT_HOST = 'blue'
SSH_PRIVATE_KEY = '~/.ssh/id_rsa'

# Outputs on the lab computer (log directories)
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
    from doodad.easy_launch.config import *
    print ("Running Something?")
except:
    print ("Something not installed")
    pass 
