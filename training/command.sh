#python -m train.py --filter_size 7\
#		   --out_dir ../out\
#		   --epochs 10\
#		   --vis_freq 512\
#		   --batch_size 32\
#		   --patience 50\
#		   models.smorphnet_double\
#		   mse\
#		   closing\
#		   complex\
#		   mnist ../mnist

python -m train.py --filter_size 7\
		   --out_dir ../out\
		   --epochs 10\
		   --patience 10\
		   models.smorphnet_double\
		   mse\
		   closing\
		   complex\
		   mnist ../mnist


