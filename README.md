<<<<<<< HEAD
The repository contains codes for our work titled "Joint learning for seismic inversion: An acoustic impedance estimation case study" accepted presented at the SEG 2020 Annual Meeting and published to SEG 2020 Expanded Abstracts. The preprint for the work may be obtained [here](https://arxiv.org/abs/2006.15474). 

The complete bibtex citation for the work is as follows:

```
@inbook{doi:10.1190/segam2020-3428378.1,
author = {Ahmad Mustafa and Ghassan AlRegib},
title = {Joint learning for seismic inversion: An acoustic impedance estimation case study},
booktitle = {SEG Technical Program Expanded Abstracts 2020},
chapter = {},
pages = {1686-1690},
year = {2020},
doi = {10.1190/segam2020-3428378.1},
URL = {https://library.seg.org/doi/abs/10.1190/segam2020-3428378.1},
}
```


The repository contains all the data used to run the codes. Clone the github repo to an appropriate directory on your machine. You may use a dedicated IDE like Pycharm or Spyder to run the `main.py` file, which will extract the data, perform training, and then use the trained models to infer on the Marmousi 2 and SEAM sections to print out the estimated 2-D profiles as well as various regression metrics between the estimated and ground-truth impedance for both datasets. Alternatively, you may use the command line to to run codes and print results, as follows:

```
cd <project root directory>
python main.py --no_wells_marmousi 50 --no_wells_seam 12 --epochs 900 --gamma 0.0001
```

In case you face problems with running the codes, please contact Ahmad Mustafa at amustafa9@gatech.edu.



=======
# SEG-2020-Spatiotemporal-modeling-for-seismic-invesion
Contains codes for our abstract accepted for presentation to SEG 2020 Annual Meeting
>>>>>>> origin/main
