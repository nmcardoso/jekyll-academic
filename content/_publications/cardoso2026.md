---
title: "AstroInspect: a web-based system to organize, assess, and visually inspect astronomical objects"
venue: Astronomical Journal
authors: |
  Natanael M. Cardoso, Claudia Mendes de Oliveira, Angela C. Krabbe, Analia V. Smith Castelli, Gustavo B. Oliveira Schwarz, Lilianne Nakazono, Ricardo Demarco, Maiara S. Carvalho, William Schoenell, Tiago Ribeiro, Antonio Kanaan and Antonio M. Saraiva
date: 2026-03-14
status: accepted
image: https://natanael.net/files/cardoso2026/astroinspect_ui.jpg
masterhead: false
pdf: https://arxiv.org/pdf/2603.04713
ads: https://ui.adsabs.harvard.edu/abs/2026arXiv260304713C%2F/abstract
files:
  - resource: Table 1
    name: table1.parquet
    url: https://astroinspect.natanael.net/publications/hydra-halpha/table1.parquet
  - resource: Table 1
    name: table1.csv
    url: https://astroinspect.natanael.net/publications/hydra-halpha/table1.csv
  - resource: Table 1
    name: table1.xml
    url: https://astroinspect.natanael.net/publications/hydra-halpha/table1.xml
abstract: >
  The rapid growth of imaging and spectroscopic surveys has intensified the need for efficient tools that support visual inspection, a practice that remains essential for tasks such as classification, catalog refinement, and validation of automated methods. Existing solutions, however, often require the use of multiple platforms and complex workflows to integrate heterogeneous data. To address this challenge, we present the first release of the AstroInspect ([https://astroinspect.github.io](https://astroinspect.github.io)), a web-based system which ensures seamless access to several astronomical resources. The system provides an intuitive graphical user interface (GUI) through which users can upload catalogs of objects defined by celestial coordinates. AstroInspect automatically enriches these catalogs with complementary information, including imaging, spectroscopic, and photometric data retrieved in real time from surveys such as the Sloan Digital Sky Survey (SDSS), the Legacy Surveys (LS), and the Southern Photometric Local Universe Survey (S-PLUS). As an example of its scientific utility, we used AstroInspect to identify H$$\alpha$$ emission-line galaxies within a 7 deg radius in the direction of the Hydra I cluster (also known as Abell 1060) by visual inspection. Using a candidate set of 981 galaxies selected from S-PLUS photometric data, we produced a catalog of 80 galaxies with confirmed H$$\alpha$$ emission. These results highlight the potential of AstroInspect to support efficient visual inspection workflows.
bibtex: |
  @article{astroinspect,
    author = {{Cardoso}, Natanael M. and {Mendes de Oliveira}, Claudia and {Krabbe}, Angela C. and {Smith Castelli}, Analia V. and {Oliveira Schwarz}, Gustavo B. and {Nakazono}, Lilianne and {Demarco}, Ricardo and {Carvalho}, Maiara S. and {Schoenell}, William and {Ribeiro}, Tiago and {Kanaan}, Antonio and {Saraiva}, Antonio M.},
    title = "{AstroInspect: a web-based system to organize, assess, and visually inspect astronomical objects}",
    journal = {Astronomical Journal},
    keywords = {Instrumentation and Methods for Astrophysics, Astrophysics of Galaxies},
    year = 2026,
    month = mar,
    eid = {arXiv:2603.04713},
    pages = {arXiv:2603.04713},
    archivePrefix = {arXiv},
    eprint = {2603.04713},
    primaryClass = {astro-ph.IM},
    adsurl = {https://ui.adsabs.harvard.edu/abs/2026arXiv260304713C},
    adsnote = {Provided by the SAO/NASA Astrophysics Data System}
  }
---

## Table 1

The Table 1 of the AstroInspect paper contains all H$$\alpha$$ emission-line galaxies within 5$$R_{200}$$ ($$\approx 7$$ deg) of the Hydra I cluster (also known as Abell 1060) {% cite abell1989 %} found by visual inspection using AstroInspect.

### Columns description


<div class="overflow-x-auto w-100">
<table class="table table-hover">
  <thead>
    <tr>
      <th>#</th>
      <th>Unit</th>
      <th>Column name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td></td><td>id</td><td>Catalog unique identifier</td></tr>
    <tr><td>2</td><td>deg</td><td>ra</td><td>Right Ascension in decimal degrees (J2000)</td></tr>
    <tr><td>3</td><td>deg</td><td>dec</td><td>Declination in decimal degrees (J2000)</td></tr>
    <tr><td>4</td><td>mag</td><td>sp_mag_u</td><td>S-PLUS DR5 magnitude in the u band</td></tr>
    <tr><td>5</td><td>mag</td><td>sp_mag_g</td><td>S-PLUS DR5 magnitude in the g band</td></tr>
    <tr><td>6</td><td>mag</td><td>sp_mag_r</td><td>S-PLUS DR5 magnitude in the r band</td></tr>
    <tr><td>7</td><td>mag</td><td>sp_mag_i</td><td>S-PLUS DR5 magnitude in the i band</td></tr>
    <tr><td>8</td><td>mag</td><td>sp_mag_z</td><td>S-PLUS DR5 magnitude in the z band</td></tr>
    <tr><td>9</td><td>mag</td><td>sp_mag_F378</td><td>S-PLUS DR5 magnitude in the F378 band (Balmer jump / [O\(_{\rm II}\)])</td></tr>
    <tr><td>10</td><td>mag</td><td>sp_mag_F395</td><td>S-PLUS DR5 magnitude in the F395 band (Ca H + K)</td></tr>
    <tr><td>11</td><td>mag</td><td>sp_mag_F410</td><td>S-PLUS DR5 magnitude in the F410 band (H\(\delta\))</td></tr>
    <tr><td>12</td><td>mag</td><td>sp_mag_F430</td><td>S-PLUS DR5 magnitude in the F430 band (G band)</td></tr>
    <tr><td>13</td><td>mag</td><td>sp_mag_F515</td><td>S-PLUS DR5 magnitude in the F515 band (Mg b triplet)</td></tr>
    <tr><td>14</td><td>mag</td><td>sp_mag_F660</td><td>S-PLUS DR5 magnitude in the F660 band (H\(\alpha\))</td></tr>
    <tr><td>15</td><td>mag</td><td>sp_mag_F861</td><td>S-PLUS DR5 magnitude in the F861 band (Ca triplet)</td></tr>
    <tr>
      <td>16-27</td>
      <td>mag</td>
      <td>sp_mag_err_<tt>[band]</tt></td>
      <td>
        S-PLUS DR5 magnitude error, where <tt>[band]</tt> is one of: 
        u, g, r, i, z, F378, F395, F410, F430, F515, F660, F861
      </td>
    </tr>
    <tr><td>28</td><td>deg</td><td>sp_A</td><td>S-PLUS DR5 profile RMS along the major axis</td></tr>
    <tr><td>29</td><td>deg</td><td>sp_B</td><td>S-PLUS DR5 profile RMS along the minor axis</td></tr>
    <tr><td>30</td><td>deg</td><td>sp_PA</td><td>S-PLUS DR5 position angle (CCW/World-x)</td></tr>
    <tr><td>31</td><td>deg</td><td>sp_radius_petro</td><td>S-PLUS DR5 Petrosian aperture radius</td></tr>
    <tr><td>32</td><td>deg</td><td>sp_radius_50</td><td>S-PLUS DR5 radius enclosing 50% of the total flux</td></tr>
    <tr><td>33</td><td>deg</td><td>sp_radius_90</td><td>S-PLUS DR5 radius enclosing 90% of the total flux</td></tr>
    <tr><td>34</td><td></td><td>sp_photoz</td><td>S-PLUS DR5 photometric redshift</td></tr>
    <tr><td>35</td><td></td><td>sp_photoz_odds</td><td>S-PLUS DR5 photometric redshift odds</td></tr>
    <tr><td>36</td><td>mag</td><td>ls_mag_g</td><td>LS DR10 magnitude in the g band</td></tr>
    <tr><td>37</td><td>mag</td><td>ls_mag_r</td><td>LS DR10 magnitude in the r band</td></tr>
    <tr><td>38</td><td>mag</td><td>ls_mag_i</td><td>LS DR10 magnitude in the i band</td></tr>
    <tr><td>39</td><td>mag</td><td>ls_mag_z</td><td>LS DR10 magnitude in the z band</td></tr>
    <tr>
      <td>40</td>
      <td></td>
      <td>ls_type</td>
      <td>
        LS DR10 morphological type (for details, see 
        <a href="https://www.legacysurvey.org/dr10/description">
          https://www.legacysurvey.org/dr10/description
        </a>)
      </td>
    </tr>
    <tr><td>41</td><td></td><td>lit_redshift</td><td>Spectroscopic redshift</td></tr>
    <tr><td>42</td><td></td><td>lit_redshift_err</td><td>Spectroscopic redshift error</td></tr>
    <tr><td>43</td><td></td><td>lit_source</td><td>Spectroscopic redshift source from literature</td></tr>
    <tr><td>44</td><td>km/s</td><td>velocity</td><td>Velocity derived from spectroscopic redshift</td></tr>
    <tr><td>45</td><td>km/s</td><td>velocity_err</td><td>Velocity error</td></tr>
    <tr>
      <td>46</td>
      <td>km/s</td>
      <td>velocity_offset</td>
      <td>
        Velocity difference between the object and the Hydra I cluster,
        available only for objects with known spectroscopic redshift
      </td>
    </tr>
    <tr>
      <td>47</td>
      <td>deg</td>
      <td>dist_proj</td>
      <td>
        Sky-projected angular distance between the object and the Hydra I cluster center
      </td>
    </tr>
    <tr>
      <td>48</td>
      <td>Mpc</td>
      <td>dist</td>
      <td>
        Distance between the object and the Hydra I cluster center,
        available only for objects with known spectroscopic redshift
      </td>
    </tr>
  </tbody>
  <caption class="text-secondary-emphasis">Notes &mdash; Columns prefixed with <tt>sp</tt> are drawn from S-PLUS DR5 (E. V. Lima et al. 2026, in preparation), while those prefixed with <tt>ls</tt> originate from Legacy Survey DR10 {% cite legacy %}. Columns prefixed with <tt>lit</tt> originate from redshift compilation from the literature {% cite erik-redshifts %}. Columns without these prefixes were derived in this work. All magnitudes are reported in the AB system, and the S-SPLUS magnitudes included in the catalog are only the auto-aperture values.</caption>
</table>
</div>