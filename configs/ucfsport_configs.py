import argparse

parser = argparse.ArgumentParser(description='STRPM')
parser.add_argument('--data_train_path', type=str, default='/kaggle/working/STRPM2/datasets/ucfsports/train.txt')
parser.add_argument('--data_val_path', type=str, default='/kaggle/working/STRPM2/datasets/ucfsports/test.txt')
parser.add_argument('--data_test_path', type=str, default='/kaggle/working/STRPM2/data/ucfsport/test.txt')
parser.add_argument('--input_length', type=int, default=4)
parser.add_argument('--real_length', type=int, default=10)
parser.add_argument('--total_length', type=int, default=10)
parser.add_argument('--img_height', type=int, default=512)
parser.add_argument('--img_width', type=int, default=512)
parser.add_argument('--sr_size', type=int, default=4)
parser.add_argument('--img_channel', type=int, default=3)
parser.add_argument('--reverse_input', type=bool, default=True)
parser.add_argument('--patch_size', type=int, default=8)
parser.add_argument('--model_name', type=str, default='strpm')
parser.add_argument('--dataset', type=str, default='ucfsport')
parser.add_argument('--num_hidden', type=int, default=128)
parser.add_argument('--D_num_hidden', type=int, default=64)
parser.add_argument('--num_layers', type=int, default=16)
parser.add_argument('--filter_size', type=int, default=(5, 5))
parser.add_argument('--stride', type=int, default=1)
parser.add_argument('--tau', type=int, default=5)
parser.add_argument('--is_training', type=bool, default=True)
parser.add_argument('--lr', type=float, default=5e-3)
parser.add_argument('--lr_d', type=float, default=5e-4)
parser.add_argument('--lr_decay', type=float, default=0.90)
parser.add_argument('--delay_interval', type=float, default=2000)
parser.add_argument('--batch_size', type=int, default=1)
parser.add_argument('--max_iterations', type=int, default=100000)
parser.add_argument('--max_epoches', type=int, default=100000)
parser.add_argument('--display_interval', type=int, default=1)
parser.add_argument('--test_interval', type=int, default=1000)
parser.add_argument('--snapshot_interval', type=int, default=1000)
parser.add_argument('--num_save_samples', type=int, default=0)
parser.add_argument('--n_gpu', type=int, default=1)
parser.add_argument('--pretrained_model_pm', type=str, default='')
parser.add_argument('--pretrained_model_d', type=str, default='')
#parser.add_argument('--pretrained_model_pm', type=str, default='pretrained_model/ucfsport/us_model_pm.ckpt-1')
#parser.add_argument('--pretrained_model_d', type=str, default='pretrained_model/ucfsport/us_model_d.ckpt-1')
parser.add_argument('--perforamnce_dir', type=str, default='/kaggle/working/STRPM2/results/ucfsport/')
parser.add_argument('--save_dir', type=str, default='/kaggle/working/STRPM2/checkpoints/ucfsport/')
parser.add_argument('--gen_frm_dir', type=str, default='/kaggle/working/STRPM2/results/ucfsport')
parser.add_argument('--scheduled_sampling', type=bool, default=True)
parser.add_argument('--sampling_stop_iter', type=int, default=20000)
parser.add_argument('--sampling_start_value', type=float, default=1.0)
parser.add_argument('--sampling_changing_rate', type=float, default=0.00005)
args = parser.parse_args()
args.tied = True