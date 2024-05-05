import os

names_train = ['humans142', 'humans143', 'humans144', 'humans160', 'humans161', 'humans162', 'humans208', 'humans209', 'humans210', 'humans241', 'humans242', 
               'humans243', 'humans256', 'humans257', 'humans258', 'humans259', 'humans260', 'humans261', 'humans268', 'humans269', 'humans270', 'humans289', 
               'humans2895', 'humans2896', 'humans2897', 'humans2898', 'humans2899', 'humans290', 'humans2900', 'humans2901', 'humans2902', 'humans2903', 'humans291', 
               'humans2910', 'humans2911', 'humans2912', 'humans2925', 'humans2926', 'humans2927', 'humans2928', 'humans2929', 'humans2930', 'humans2931', 'humans2932', 
               'humans2933', 'humans2937', 'humans2938', 'humans2939', 'humans2943', 'humans2944', 'humans2945', 'humans2946', 'humans2947', 'humans2948', 'humans2949', 
               'humans2950', 'humans2951', 'humans2958', 'humans2959', 'humans2960', 'humans2961', 'humans2962', 'humans2963', 'humans2964', 'humans2965', 'humans2966', 
               'humans2967', 'humans2968', 'humans2969', 'humans2970', 'humans2971', 'humans2972', 'humans2973', 'humans2974', 'humans2981', 'humans2982', 'humans2983', 
               'humans2984', 'humans2985', 'humans2986', 'humans2987', 'humans2988', 'humans2989', 'humans2993', 'humans2994', 'humans2995', 'humans2996', 'humans2997', 'humans2998', 'humans3008', 
               'humans3009', 'humans301', 'humans3010', 'humans3011', 'humans3012', 'humans3013', 'humans3014', 'humans3015', 'humans3016', 'humans3017', 'humans3018', 'humans3019', 'humans302', 
               'humans3020', 'humans3021', 'humans3022', 'humans3029', 'humans303', 'humans3030', 'humans3031', 'humans3032', 'humans3033', 'humans3034', 'humans3035', 'humans3036', 'humans3037', 
               'humans3038', 'humans3039', 'humans3040', 'humans3044', 'humans3045', 'humans3046', 'humans3050', 'humans3051', 'humans3052', 'humans3053', 'humans3054', 'humans3055', 'humans3065', 
               'humans3066', 'humans3067', 'humans3074', 'humans3075', 'humans3076', 'humans3077', 'humans3078', 'humans3079', 'humans3080', 'humans3081', 'humans3082', 'humans3086', 'humans3087', 
               'humans3088', 'humans3092', 'humans3093', 'humans3094', 'humans3095', 'humans3096', 'humans3097', 'humans3107', 'humans3108', 'humans3109', 'humans3110', 'humans3111', 'humans3112', 
               'humans3116', 'humans3117', 'humans3118', 'humans3122', 'humans3123', 'humans3124', 'humans3125', 'humans3126', 'humans3127', 'humans3131', 'humans3132', 'humans3133', 'humans3134', 
               'humans3135', 'humans3136', 'humans3140', 'humans3141', 'humans3142', 'humans3143', 'humans3144', 'humans3145', 'humans3146', 'humans3147', 'humans3148', 'humans3152', 'humans3153', 
               'humans3154', 'humans3158', 'humans3159', 'humans3160', 'humans3161', 'humans3162', 'humans3163', 'humans3167', 'humans3168', 'humans3169', 
               'humans3170', 'humans3171', 'humans3172', 'humans3197', 'humans3198', 'humans3199', 'humans3215', 'humans3216', 'humans3217', 'humans3245', 'humans3246', 'humans3247', 'humans3248', 
               'humans3249', 'humans3250', 'humans511', 'humans512', 'humans513', 'humans517', 'humans518', 'humans519', 'humans550', 'humans551', 'humans552', 'humans553', 'humans554', 'humans555', 
               'humans613', 'humans614', 'humans615', 'humans67', 'humans68', 'humans69', 'humans706', 'humans707', 'humans708', 'humans715', 'humans716', 'humans717', 'humans739', 'humans740', 'humans741', 
               'humans745', 'humans746', 'humans747', 'humans748', 'humans749', 'humans750', 'humans754', 'humans755', 'humans756', 'humans760', 'humans761', 'humans762', 'humans766', 'humans767', 'humans768', 
               'humans769', 'humans770', 'humans771', 'humans772', 'humans773', 'humans774', 'humans784', 'humans785', 'humans786', 'humans787', 'humans788', 'humans789', 'humans796', 'humans797', 'humans798', 
               'humans802', 'humans803', 'humans804', 'humans805', 'humans806', 'humans807', 'humans808', 'humans809', 'humans810', 'humans811', 'humans812', 'humans813', 'humans814', 'humans815', 'humans816', 
               'humans823', 'humans824', 'humans825', 'humans826', 'humans827', 'humans828', 'humans3353', 'humans3356', 'humans3357', 'humans3358', 'humans3362', 'humans3373', 'humans3387', 'humans3392', 'humans3393', 'humans3412', 'humans3413']

names_val = ['humans3676', 'humans3677', 'humans3679', 'humans3681', 'humans3683', 'humans3684', 
             'humans3685', 'humans3687', 'humans3689', 'humans3690', 'humans3691', 'humans3692', 'humans3693', 'humans3695', 'humans3698', 
             'humans3699', 'humans3701', 'humans3702', 'humans3703', 'humans3704', 'humans3706', 'humans3711', 'humans3715', 'humans3719', 'humans3748', 
             'humans3756', 'humans3768', 'humans3777', 'humans3784', 'humans3794', 'humans3801', 'humans3352', 'humans3354', 'humans3364', 'humans3399']




def remove_corrupted_files(source_folder, list_of_files):

    images_folder = os.path.join(source_folder, 'images')
    labels_folder = os.path.join(source_folder, 'labels')


    for file in list_of_files:
        image_path = os.path.join(images_folder, file + '.jpg')
        label_path = os.path.join(labels_folder, file + '.txt')

        os.remove(image_path)
        os.remove(label_path)

        print(f'{file} removed ')







