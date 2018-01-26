


configurations = {
    # same configuration as original work
    # https://github.com/shelhamer/fcn.berkeleyvision.org
    0: dict(
        max_iteration=100000,
        lr=1.0e-10,
        momentum=0.99,
        weight_decay=0.0005,
        interval_validate=4000,
    ),

    # python train_*.py -g 0 -c 1
    1: dict(
        max_iteration=100,
        lr=0.01,             # changed learning rate
        lr_decay_epoch=None, # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=10,
        optim='Adam',
        batch_size=100,
    ),

    2: dict(
        max_iteration=8670,    # num_iter_per_epoch = ceil(num_images/batch_size)
        lr=0.01,               # high learning rate
        lr_decay_epoch=None,   # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=10,
        optim='Adam',
        batch_size=250,
    ),

    3: dict(
        # num_iter_per_epoch = ceil(num_images/batch_size)
        max_iteration=8670,  # 10 epochs on subset of images
        lr=0.001,            # lowered learning rate
        lr_decay_epoch=None, # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=10,
        optim='Adam',
        batch_size=250,
    ),
    # ---------------------------------------------------------------------------------

    # ResNet-50 on UMDFaces: stage 1
    4: dict(
        # num_iter_per_epoch = ceil(num_images/batch_size)
        max_iteration=42180,  # 30 epochs on full dataset (about 10 hours)
        lr=0.001,             # learning rate
        lr_decay_epoch=None,  # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=50,
        optim='Adam',
        batch_size=250,
    ),

    # ResNet-50 on UMDFaces: stage 2
    5: dict(
        # num_iter_per_epoch = ceil(num_images/batch_size)
        max_iteration=42180,  # 30 epochs on full dataset
        lr=0.0001,            # lowered learning rate
        lr_decay_epoch=None,  # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=50,
        optim='Adam',
        batch_size=250,
    ),

    # ResNet-50 on UMDFaces: stage 3
    6: dict(
        # num_iter_per_epoch = ceil(num_images/batch_size)
        max_iteration=42180,   # 30 epochs on full dataset
        lr=0.00001,            # lowered learning rate
        lr_decay_epoch=None,   # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=50,
        optim='Adam',
        batch_size=250,
    ),
    # ---------------------------------------------------------------------------------

    # ResNet-101 on VGGFace2: stage 1
    7: dict(
        # num_iter_per_epoch = ceil(num_images/batch_size)
        max_iteration=267630,  # 30 epochs on full dataset
        lr=0.001,              # learning rate
        lr_decay_epoch=None,   # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=500,
        optim='Adam',
        batch_size=350,        # DataParallel over 7 gpus
    ),

    # python vgg-face-2/train_resnet_vggface.py -c 8 -m PATH-TO-CFG-7-SAVED-MODEL
    8: dict(
        # num_iter_per_epoch = ceil(num_images/batch_size)
        max_iteration=267630,  # 30 epochs on full dataset
        lr=0.0001,             # lowered learning rate
        lr_decay_epoch=None,   # disable automatic lr decay
        momentum=0.9,  
        weight_decay=0.0005,
        interval_validate=500,
        optim='Adam',
        batch_size=350,        # DataParallel over 7 gpus
    ),


}



