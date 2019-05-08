CONFIG = {
    'gal_type': 'wldeblend',
    'psf_type': 'gauss',
    'shear_scene': True,
    'n_coadd': 1,  # ignored for this sim
    'scale': 0.2,
    'dim': 300,
    'n_coadd_psf': 1,
    'gal_kws': {
        'survey_name': 'LSST',
        'bands': ('i')},
    'psf_kws': {'fwhm': 0.7}
}
