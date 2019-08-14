train_id=$1

if [ $train_id = "trainv1" ]; then
    list_param="--tsne_input=feature_beard_trainv1.npy --target=target_beard_trainv1.npy"
elif [ $train_id = "trainv2" ]; then
    list_param="--tsne_input=feature_beard_trainv2.npy --target=target_beard_trainv2.npy"
elif [ $train_id = "trainv3" ]; then
    list_param="--tsne_input=feature_beard_trainv3.npy --target=target_beard_trainv3.npy"
fi

echo $list_param


CUDA_VISIBLE_DEVICES=1,2,3 python -u tsne.py \
 --root /lustre/home/mcxu/experiments/super-resolution/SRGAN-reg-eng \
 --sr_matri ../tsne/v2-1,0.1/netD_epoch_4_1_iter_180000.pth_sr.npy \
 --hr_matri ../tsne/v2-1,0.1/netD_epoch_4_1_iter_180000.pth_hr.npy \
 --hr_restore_matri ../tsne/v2-1,0.1/netD_epoch_4_1_iter_180000.pth_hr_restore.npy \
 --out result \
#  --tsne_input feature_person_trainv1.npy \
#  --target target_person_trainv1.npy \
