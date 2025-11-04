---
title: "EpigraphiCy: An Open-Source Platform for the Documentation, Analysis, and Online Dissemination of Ancient Inscriptions"
tags:
  - Python
  - Django
  - Content Model
  - Ancient Inscriptions
  - Open-Source Platform
  - Online Dissemination
  - Documentation
  - Dissemination
  - Analysis
authors:
  - name: Avgoustinos Avgousti
    orcid: 0000-0002-9116-8217
    affiliation: 1
  - name: Christos Fiakkou
    orcid: 0009-0008-8147-6751
    affiliation: 1
affiliations:
  - name: The Cyprus Institute, Science and Technology in Archaeology and Culture Research Center (STARC), Nicosia, Cyprus
    index: 1
date: 2025-10-30
---

# Summary

**EpigraphiCy** is an open-source framework designed for the sustainable management, visualization, and online dissemination of ancient inscriptions (Bozia et al., 2014; Barmpoutis, 2013). It enables researchers and institutions to publish 2D and 3D epigraphic data in accessible, interoperable, and reusable formats. Developed initially to support the *Venetian Inscriptions in Cyprus* project, EpigraphiCy has evolved into a general-purpose platform promoting open access, digital preservation, and knowledge sharing in the field of archaeology.

# Statement of Need

The digitization of archaeological materials such as ancient inscriptions has advanced significantly in recent years, facilitated by affordable methods for producing high-resolution images, 3D models, and digital databases (Hernández-Muñoz, 2023; Pendić & Molloy, 2024). However, the online dissemination of this valuable knowledge remains limited. Despite technological progress, much of the resulting 3D or photographic data remains inaccessible beyond institutional repositories (Bozia et al., 2014; Lasagni, 2020).

This situation leaves much of the digital content effectively “locked” within academic publications or internal archives, restricting access for the broader research community and the public. Sustainable preservation and open sharing of epigraphic material therefore continue to pose major challenges.  

To address this gap, **EpigraphiCy** was developed as a cost-effective, open-source framework for managing, visualizing, and publishing ancient inscriptions. By combining sustainable preservation practices with open-access dissemination, it provides researchers and institutions with a practical solution for ensuring the long-term accessibility, interoperability, and reuse of epigraphic data.

Initially developed for the *Venetian Inscriptions in Cyprus* project, the platform produced the first open-access portal dedicated to Venetian Renaissance epigraphy. Building on this success, its underlying framework has evolved into a flexible, general-purpose system applicable to a wide range of archaeological contexts.

# Major Features

At the core of EpigraphiCy lies a flexible and extensible content model designed to accommodate the complex descriptive, visual, and spatial requirements of epigraphic documentation. Each inscription record captures detailed metadata about the artifact—such as title, location, material, dimensions, writing type, language, and preservation state—along with interpretive and bibliographic data including diplomatic and edited transcriptions, translations, and EpiDoc XML files. This metadata model aligns with best practices in digital epigraphy and spatial humanities (Lasagni, 2020).

A key feature of the system is its ability to integrate and dynamically display high-resolution images and 3D models stored on external object storage services, ensuring scalability and long-term sustainability (Hernández-Muñoz, 2023; Archaeology Data Service, 2016). Researchers can associate multiple images per record, offering diverse visual perspectives, while 3D models can be interactively embedded for close examination of surface textures and inscriptions.

EpigraphiCy also includes an interactive geospatial interface that visualizes inscriptions on an integrated map. Each record is georeferenced using precise latitude and longitude values, allowing users to explore inscriptions within their geographical and architectural contexts. This spatial visualization supports grouping related content, such as all inscriptions associated with a particular monument, site, or building complex.

For example, a castle can be represented through its 3D architectural model, while individual inscriptions found on or within it are displayed in relation to that structure. This feature enables users to study spatial correlations and contextual meanings—an approach recognized as transformative in digital epigraphy (Lasagni, 2020).

By combining structured metadata, geospatial visualization, and interactive 3D integration, EpigraphiCy moves beyond traditional cataloguing systems to offer a rich, immersive environment for the preservation, analysis, and online dissemination of ancient inscriptions and their broader architectural and cultural contexts.

# Acknowledgements

We thank the research team and technical collaborators of the *Venetian Inscriptions in Cyprus* project, whose work inspired the creation of EpigraphiCy.

# Conflicts of Interest

The authors declare no conflicts of interest.

# References

Archaeology Data Service / Digital Antiquity. (2016). *3D Models in Archaeology: Aims and Objectives*. Archaeology Data Service.  

Barmpoutis, A. (2013). *Digital Epigraphy Toolbox*. Humanities Commons.  

Bozia, E., Barmpoutis, A., & Wagman, R. S. (2014). *Open-Access Epigraphy: Electronic Dissemination of 3D Digitized Archaeological Material*. In *Information Technologies for Epigraphy and Digital Cultural Heritage in the Ancient World (EAGLE 2014)* (pp. 421–435).  

Hernández-Muñoz, Ó. (2023). *Analysis of Digitized 3D Models Published by Archaeological Museums*. *Heritage*, 6(5), 3885–3902. https://doi.org/10.3390/heritage6050206  

Lasagni, C. (2020). *The Places of Inscriptions: From Epigraphy to Digital Epigraphy*. *Historika*, 10.  

Pendić, J., & Molloy, B. (2024). *The Use of 3D Documentation for Investigating Archaeological Artefacts*. In *The 3 Dimensions of Digitalised Archaeology* (pp. 9–26). Springer.  




