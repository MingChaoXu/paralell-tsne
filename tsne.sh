train_id=$1

if [ $train_id = "trainv1" ]; then
    list_param="--tsne_input=feature_beard_trainv1.npy --target=target_beard_trainv1.npy"
elif [ $train_id = "trainv2" ]; then
    list_param="--tsne_input=feature_beard_trainv2.npy --target=target_beard_trainv2.npy"
elif [ $train_id = "trainv3" ]; then
    list_param="--tsne_input=feature_beard_trainv3.npy --target=target_beard_trainv3.npy"
fi

echo $list_param


python -u tsne_beard-parall.py \
 --root '' \
 $list_param \
 --out checkpair \
#  --tsne_input feature_person_trainv1.npy \
#  --target target_person_trainv1.npy \
