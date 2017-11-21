import numpy as np

sierpinski_nums = [
    [0.5, 0.0, 0.0, 0.5, 0.0, 0.0],
    [0.5, 0.0, 0.0, 0.5, 0.5, 0.0],
    [0.5, 0.0, 0.0, 0.5, 0.25, np.sqrt(3.)/4],
]

sierpinski_probs = [
    1./3,
    1./3,
    1./3,
]

sierpinski = (sierpinski_nums, sierpinski_probs)

barnsley_nums = [
    [.85, .04, -.04, .85, .0, 1.6],
    [.2, -.26, .23, .22, .0, 1.6],
    [-.15, .28, .26, .24, .0, .44],
    [.0, .0, .0, .16, .0, .0],
]

barnsley_probs = [
    .73,
    .13,
    .11,
    .03,
]

barnsley = (barnsley_nums, barnsley_probs)

dragon_nums = [
    [.824074, .281482, -.212346, .864198, -1.882290, -0.110607],
    [.088272, .520988, -.463889, -.377778, .785360, 8.095795],
]

dragon_probs = [
    .787473,
    .212527,
]

dragon = dragon_nums, dragon_probs

levy_nums = [
    [.5, -.5, .5, .5, .0, .0],
    [.5, .5, -.5, .5, .5, .5],
]

levy_probs = [
    .5,
    .5,
]

levy = levy_nums, levy_probs