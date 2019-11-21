import argparse
from pathlib import Path

"""
set configuration arguments as class attributes
"""


class Config(object):
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      setattr(self, k, v)


"""
get configuration arguments
"""


def get_config(**kwargs):
  parser = argparse.ArgumentParser()

  parser.add_argument('--mode', type=str, default='train')

  # LstmGan model args
  parser.add_argument('--input_size', type=int, default=2048)
  parser.add_argument('--hidden_size', type=int, default=1024)
  parser.add_argument('--batch_size', type=int, default=256)
  parser.add_argument('--num_workers', type=int, default=12)
  parser.add_argument('--num_layers', type=int, default=2)
  parser.add_argument('--summary_rate', type=int, default=0.2)

  # train
  parser.add_argument('--n_epochs', type=int, default=500)
  parser.add_argument('--sum_learning_rate', type=float, default=1e-4)
  parser.add_argument('--dis_learning_rate', type=float, default=1e-5)
  parser.add_argument('--dis_start_batch', type=int, default=15)
  #   # features
  parser.add_argument('--train_features_list', type=str, default=Path(
    '/nas/team-space/experiments/video-lstm/resnet50-features-02-10-2019/features-train.list'))
  parser.add_argument('--val_features_list', type=str, default=Path(
    '/nas/team-space/experiments/video-lstm/resnet50-features-02-10-2019'
    '/features-val.list'))
  parser.add_argument('--nb_samples', type=int, default=50000)

  # timesteps
  parser.add_argument('--min_timesteps', type=int, default=64)
  parser.add_argument('--max_timesteps', type=int, default=64)

  # log
  parser.add_argument('--log_dir', type=str, default=Path('logs'))
  parser.add_argument('--detail_flag', type=bool, default=True)

  # mode save path
  parser.add_argument('--model_save_dir', type=str,
                      default=Path('/tmp/pycharm_project_753/models'))

  args = parser.parse_args()
  # namespace -> dictionary
  args = vars(args)
  args.update(kwargs)

  return Config(**args)
