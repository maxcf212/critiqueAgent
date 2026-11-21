Mission Assignment: Final Report

AERO9500 - T3 2020

Space Systems Architectures and Orbits

## Executive Summary

This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite for monitoring coral bleaching on the Great Barrier Reef. The 50 kg satellite carries a multispectral imager with a 5 m ground sample distance and a 60 km swath. It is launched as a rideshare passenger on a Vega C from Kourou in 2025 into a circular sun-synchronous orbit at 600 km altitude and 97.79° inclination, with a period of 96.7 minutes. No orbital manoeuvres are needed. The satellite is operated by the Australian Institute of Marine Science through the Mount Pleasant ground station in Tasmania, which sees six passes a day with a mean duration of 9.7 minutes; this gives about three times the downlink capacity the imaging plan needs. The mission lasts five years and ends with a passive drag sail that removes the satellite in about two years, well inside the 25-year guideline. The design is supported by STK simulations and by hand calculations of the orbit, coverage, data budget and orbital decay.

## Contents

Executive Summary  
1 Introduction  
2 Mission Design  
2.1 Spacecraft overview  
2.2 Launch  
2.3 Orbit  
2.4 Ground Control & Communications  
2.5 Mission Duration & EOL  
3 Conclusion  
Bibliography  
Appendix A: STK files and settings

## 1 Introduction

Coral reefs harbour some of the most diverse species of life on the planet, but this is not even the full extent of their nurture. Hundreds of millions of humans rely on reefs for food, natural protection, jobs, and tourism. Over the last century, human-induced environmental change – as a result of increased burning of fossil fuels and deforestation – has put huge ecosystems at risk. Oceans have become 30 percent more acidic since the industrial revolution [1], and rising sea temperatures cause the bleaching of coral reefs. These bleaching events are destructive enough to wipe out entire reefs.

Australia’s Great Barrier Reef is the largest coral reef in the world, spread over 344,400 km². It is one of the most complex, vast, and flourishing ecosystems on Earth, but it is due to suffer several more bleaching events in the coming years. In 2016, a bleaching event killed 30 percent of the reef’s coral. In 2017, another 20 percent perished [2].

**Primary mission.** Traditionally, coral bleaching was monitored by aerial surveys, and more recently by satellite sea surface temperature monitoring. However, while high temperatures can lead to bleaching, temperature is not a direct indicator that bleaching is occurring, or of its severity. Existing satellite products of the reef are also coarse: its depths have only been mapped to a resolution of 100 metres per pixel [3]. Colour and tone changes of the seafloor, where lighter hues indicate bleaching, can be detected directly in high-resolution images [4], and fluid lensing combined with machine learning has been used from aircraft to remove the distortion caused by waves [5], [6]. The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution, so that bleaching is mapped directly and any part of the reef can be revisited within about five days.

**Number of spacecraft.** Other Earth observation systems use constellations of satellites spaced out in the same orbit. ZYZZsat does not require such constant coverage, because bleaching events develop over days and weeks. One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch. Section 2.3 shows the revisit time that one satellite achieves.

**Users.** The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef; AIMS would control the satellite and process the images. The customers are the Great Barrier Reef Marine Park Authority, which uses bleaching maps to direct in-water surveys and management responses; CSIRO and university researchers, who use the multi-year image archive; and the Bureau of Meteorology, which combines the images with its sea surface temperature products. The data would be openly available, and the mission is funded by the Australian Government as a public service.

## 2 Mission Design

The mission is described in five parts: the spacecraft, launch, orbit, ground control and communications, and mission duration and end of life (EOL).

### 2.1 Spacecraft overview

Table 1 lists the main properties of the spacecraft that the rest of the design depends on.

Table 1: ZYZZsat spacecraft summary.

| Property | Value | Reason |
|---|---|---|
| Mass and size | 50 kg; 0.5 m × 0.5 m × 0.6 m | Microsatellite class, compatible with rideshare dispensers (Section 2.2) |
| Payload | Multispectral pushbroom imager, 4 visible bands, 12,000 pixels across track | Gives a 5 m ground sample distance and a 60 km swath at 600 km (Section 2.3) |
| Telescope aperture | 0.10 m | Diffraction limit for 5 m at 600 km is 1.22 × 0.5 µm × 600 km / 5 m = 0.073 m |
| Pointing | Three-axis stabilised, up to ±25° off-nadir roll | Widens the area that can be reached on each pass |
| Power | Body-mounted and deployable solar panels with a battery | The battery carries the satellite through an eclipse of about 34 minutes each orbit |
| Propulsion | None | No manoeuvres are required (Section 2.3); disposal is by drag sail (Section 2.5) |
| Communications | S-band for command and telemetry, X-band downlink at 50 Mbit/s | Section 2.4 |

### 2.2 Launch

The satellite is too small to justify a dedicated rocket, so it will be launched as a rideshare ("piggyback") passenger. The factors considered in choosing the launch are the launch service provider and its record, whether the rocket can reach the required orbit, and whether the other passengers are going to the same orbit, because all passengers on a rideshare flight are released into nearly the same orbit.

The launch site latitude matters less for this mission than for most. A site near the equator gains the most from the Earth's rotation only for eastward launches [7]. ZYZZsat needs a retrograde orbit, launched slightly west of north, so the Earth's rotation is a small penalty rather than a benefit. What matters is that the site has a clear launch corridor towards the pole and that its latitude is lower than 180° minus the inclination, so the orbit can be reached directly.

The satellite would take about four years to be launch-ready, so launches from 2025 are considered. Two rideshare services to sun-synchronous orbit exist today and are compared in Table 2.

Table 2: Rideshare launch options for a 50 kg satellite to sun-synchronous orbit.

| | Vega / Vega C Small Spacecraft Mission Service (SSMS) | Falcon 9 SmallSat Rideshare |
|---|---|---|
| Provider and site | Arianespace; Guiana Space Centre, Kourou (5.2°N) | SpaceX; United States |
| Capacity | Vega: about 1,500 kg to a 700 km polar orbit [8]; Vega C increases this | 200 kg per port as a baseline |
| Record | Proof-of-concept flight VV16 placed 53 satellites into sun-synchronous orbits in September 2020 [9] | Rideshare flights to sun-synchronous orbit offered about every four months [10] |
| Risk | Vega C has not yet flown; its first flight is planned for 2021 | Operational vehicle |

The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025, because the SSMS dispenser was designed for microsatellites of this size and the service has already flown successfully on Vega. Kourou's surroundings are sparsely populated and launches towards the north pass over the Atlantic Ocean. If Vega C is not in service or has no flight to a suitable orbit, the fallback is the Falcon 9 rideshare service, which is already operating; the satellite's mass and size fit both. The newer Vega E is not relied on because it has not been built.

The launch azimuth β needed to reach the inclination i from latitude φ is found from sin β = cos i / cos φ:

sin β = cos 97.79° / cos 5.2° = −0.1355 / 0.9959 = −0.136, so β = −7.8°

The launcher therefore flies 7.8° west of north. For a sun-synchronous orbit the launch time is fixed by the local time required at the node, so there is one launch opportunity each day.

### 2.3 Orbit

Underwater imaging by satellite is difficult after just a few metres of water, because light is distorted by waves [6]. It is therefore important that the satellite sees the reef under the same lighting each time, so that images can be compared. The most suitable orbit is a low-Earth sun-synchronous orbit: the satellite passes over any given latitude at the same local mean solar time each day. Many Earth observation satellites use this orbit, including the passengers of flight VV16 [9]. Figure 1 shows the orbit in STK.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//d6dc1cac-c230-4c7a-9a5c-f2c7dd26a135/markdown_0/imgs/img_in_image_box_130_747_583_1079.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-11-11T11%3A56%3A26Z%2F-1%2F%2Ffb27dfe19b26ba48a51fa3bcc125a81af83aed31585ca6b2c7b951df7dd69929" alt="Image" width="38%" /></div>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//d6dc1cac-c230-4c7a-9a5c-f2c7dd26a135/markdown_0/imgs/img_in_image_box_611_746_1058_1080.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-11-11T11%3A56%3A26Z%2F-1%2F%2F50eb7ec82c814cbfef8137dab9549b535e6453e63ba300d2ca7712787a1e6d05" alt="Image" width="37%" /></div>

Figure 1: STK 3D view of the ZYZZsat orbit at two times 12 hours apart (generated in STK 11).

The orbit is near-polar and retrograde, so over time the satellite passes over all latitudes up to 82°. This also allows the mission to be extended to other coral reefs.

**Altitude.** The altitude is a trade between resolution and swath. A higher altitude gives a wider swath but a coarser image, which is undesirable for detecting colour change on individual reefs. Table 3 shows the trade for the imager in Table 1.

Table 3: Imaging geometry at the chosen altitude of 600 km.

| Quantity | Calculation | Result |
|---|---|---|
| Ground sample distance | Requirement from the primary mission | 5 m |
| Swath width | 12,000 pixels × 5 m | 60 km |
| Field of view | 2 × arctan(30 km / 600 km) | 5.7° |
| Area reachable with ±25° roll | 2 × 600 km × tan 25° | 560 km |
| Spacing of ground tracks on one day (equator) | 2π × 6,378 km × 5,801 s / 86,164 s | 2,698 km |
| Days to reach any point of the reef | 2,698 km / 560 km | about 5 days |
| Days for a complete nadir-only mosaic | 2,698 km / 60 km | about 45 days |

The widest part of the reef is roughly 250 km, so it cannot be covered in one 60 km strip. Each pass images one strip of the reef, and strips are compiled into a mosaic. Using roll pointing, any reef that is reported to be bleaching can be imaged within about five days, which is fast enough for events that develop over weeks. A complete map of the reef directly from overhead takes about 45 days. A lower altitude would improve resolution but would lengthen both times and increase drag, and a higher altitude would need a larger telescope for the same 5 m, so 600 km is chosen.

**Inclination.** For the orbit to be sun-synchronous, the right ascension of the ascending node (RAAN) must move east by 360° per year, which is 0.9856° per day or 1.991 × 10⁻⁷ rad/s [11]. This movement is caused by the Earth's oblateness (J2), and its rate is

dΩ/dt = −(3/2) J2 (R/a)² n cos i

With J2 = 1.0826 × 10⁻³, R = 6,378 km, a = 6,978 km and mean motion n = √(μ/a³) = 1.0831 × 10⁻³ rad/s:

cos i = −(1.991 × 10⁻⁷) / (1.5 × 1.0826 × 10⁻³ × 0.8354 × 1.0831 × 10⁻³) = −0.1355, so i = 97.79°

This agrees with the STK value of 97.7924°. Because the rate depends on cos i, the required inclination changes with altitude, as plotted in Figure 2. If the rideshare flight releases its passengers lower, for example at 530 km, the inclination for sun-synchronism would be about 97.5° and the analysis below would be repeated for that orbit.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//d6dc1cac-c230-4c7a-9a5c-f2c7dd26a135/markdown_1/imgs/img_in_chart_box_206_753_964_1361.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-11-11T11%3A56%3A28Z%2F-1%2F%2Fab54c8928c7b91dfcbaad61b2127720890a3e65aa3b63eb6add7552ff06abf65" alt="Image" width="63%" /></div>

Figure 2: Inclination required for a sun-synchronous orbit as a function of altitude.

**Orbital elements.** The orbit is circular, so it has no perigee and two of the six classical orbital elements, the argument of perigee and the true anomaly, are undefined. They are replaced by the argument of latitude, the angle from the ascending node to the satellite. Table 4 gives the elements.

Table 4: Orbital elements of ZYZZsat at the scenario epoch, 3 Feb 2025 00:00:00 UTCG (mean elements, J2000 frame).

| Element | Value | Description |
|---|---|---|
| Semi-major axis (a) | 6,978 km | Earth equatorial radius of 6,378 km plus the altitude of 600 km |
| Eccentricity (e) | 0 | Circular orbit |
| Inclination (i) | 97.79° | Required for sun-synchronism at 600 km (calculated above) |
| Right ascension of ascending node (Ω) | 27.33° | Value in the STK scenario at the epoch. It fixes the orientation of the orbit plane relative to the Sun and is set by the time of launch, not by the launch site. It moves east by 0.9856° per day |
| Argument of latitude (u) | 0° at the epoch | Increases by 360° every orbit |
| Period | 96.7 min | T = 2π√(a³/μ) = 5,801 s; 14.9 orbits per day |

In the STK ground track the satellite crosses the reef on the descending (southbound) half of the orbit at about 08:45 local mean solar time. A morning crossing is chosen because there is usually less convective cloud over tropical water in the morning and the sun is not high enough to cause strong sun glint. The satellite is not in sunlight all the time: with this node time it is in the Earth's shadow for about 34 minutes of each orbit, which sizes the battery in Table 1.

**Manoeuvres.** No orbital manoeuvres are required. The rideshare launch releases the satellite directly into its operational orbit, and Section 2.5 shows that drag lowers the orbit by only about 11 km over the five-year mission, which does not affect imaging. The satellite therefore carries no propulsion. Disposal at end of life uses a passive drag sail, which is not a manoeuvre.

### 2.4 Ground Control & Communications

A ground station receives the data whenever the satellite is above its horizon. A near-polar orbit passes over high latitudes on every orbit and over low latitudes only a few times a day, so a station at a higher latitude sees more passes [12]. A station inside Australia is preferred because the operator and customers are Australian: data does not have to be requested from another country, and licensing is simpler.

The Mount Pleasant Radio Observatory near Hobart, Tasmania (42.8°S, 147.4°E) is selected. It is the most southerly of the suitable Australian sites, it is owned and operated by the University of Tasmania, and it has a 26 m and a 12 m antenna [13]. The 12 m antenna is far larger than a 50 kg satellite's downlink needs. Mount Pleasant is a radio astronomy and geodesy site, so this design assumes that an S-band transmitter and an X-band receiver are added to the 12 m antenna. If that is not possible, a commercial ground station at a similar latitude can be used without changing the analysis below.

STK 11 was used to calculate when the satellite is above the horizon at Mount Pleasant. Table 5 lists the first fifteen accesses.

Table 5: STK access report, ZYZZsat to Mount Pleasant Radio Observatory (elevation above 0°).

| Access | Start time (UTCG) | Stop time (UTCG) | Duration (s) |
|---|---|---|---|
| 1 | 3 Feb 2025 09:28:12.575 | 3 Feb 2025 09:30:44.204 | 151.629 |
| 2 | 3 Feb 2025 11:00:03.048 | 3 Feb 2025 11:12:34.450 | 751.402 |
| 3 | 3 Feb 2025 12:36:08.251 | 3 Feb 2025 12:47:32.331 | 684.080 |
| 4 | 3 Feb 2025 20:22:38.436 | 3 Feb 2025 20:26:45.353 | 246.918 |
| 5 | 3 Feb 2025 21:53:04.550 | 3 Feb 2025 22:05:15.325 | 730.775 |
| 6 | 3 Feb 2025 23:29:01.550 | 3 Feb 2025 23:40:54.563 | 713.012 |
| 7 | 4 Feb 2025 09:38:38.911 | 4 Feb 2025 09:44:43.938 | 365.026 |
| 8 | 4 Feb 2025 11:11:59.256 | 4 Feb 2025 11:24:43.226 | 763.970 |
| 9 | 4 Feb 2025 12:48:19.210 | 4 Feb 2025 12:59:06.894 | 647.684 |
| 10 | 4 Feb 2025 20:33:19.899 | 4 Feb 2025 20:39:34.976 | 375.077 |
| 11 | 4 Feb 2025 22:04:51.394 | 4 Feb 2025 22:17:20.866 | 749.472 |
| 12 | 4 Feb 2025 23:41:24.179 | 4 Feb 2025 23:52:43.527 | 679.348 |
| 13 | 5 Feb 2025 09:49:53.005 | 5 Feb 2025 09:57:52.867 | 479.862 |
| 14 | 5 Feb 2025 11:23:57.461 | 5 Feb 2025 11:36:47.622 | 770.160 |
| 15 | 5 Feb 2025 13:00:32.812 | 5 Feb 2025 13:10:36.194 | 603.382 |
| Minimum (access 1) | | | 151.629 |
| Maximum (access 14) | | | 770.160 |
| Mean | | | 580.786 |
| Total | | | 8,711.797 |

There are six passes each day, three in the evening and three in the morning (UTC), and the mean pass lasts 580.8 s, or 9.7 minutes. The longest pass, 770 s, matches the hand-calculated maximum for a horizon-to-horizon pass at 600 km (771 s). Over 3 and 4 February the total contact averages 57 minutes per day. Passes below 10° elevation are not usable for a high-rate downlink; the part of an overhead pass above 10° is 510 s of 771 s, so about 60 percent of the contact time, or 34 minutes per day, is counted.

Table 6: Daily data budget.

| Quantity | Calculation | Result |
|---|---|---|
| Area imaged per day | One strip over the reef: 60 km × 1,000 km | 60,000 km² |
| Raw data | 60,000 km² × 40,000 pixels/km² × 4 bands × 12 bits | 115 Gbit |
| After 4:1 compression | 115 / 4 | 29 Gbit |
| Downlink capacity | 50 Mbit/s × 2,000 s (34 minutes) | 100 Gbit |
| Margin | 100 / 29 | 3.5 |

The downlink capacity is about three and a half times the daily data volume, so all images taken in a day reach the ground within the next day, even if two of the six passes are lost. A full link budget for the X-band downlink has not been calculated in this report and is the main item of further work for this segment.

The reef is imaged in daylight on the descending half of the orbit, shown in Figure 3. Figure 4 shows both halves of the orbit and the frequent passes over Tasmania. There are short periods when the satellite can see both the reef and the ground station, which could be used to downlink an image as soon as it is taken, although the mission does not depend on this.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//a52aebe2-08a4-4028-8134-e00e38ca5de8/markdown_1/imgs/img_in_chart_box_143_189_1047_657.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-11-11T11%3A56%3A41Z%2F-1%2F%2Fccf99f96bbb62f4c7e561dbe819569fe0be7bb12d77461a42f22dd79d877964c" alt="Image" width="75%" /></div>

Figure 3: Ground track of the descending (daylight) half of orbits 1–15, STK 2D view at 3 Feb 2025 22:03:00 UTCG.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//a52aebe2-08a4-4028-8134-e00e38ca5de8/markdown_1/imgs/img_in_image_box_143_1020_1046_1477.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-11-11T11%3A56%3A42Z%2F-1%2F%2Ff146b20b15854c7d968a739da14bf97e0f8b79a1138d01ebd9a36159d9234cfb" alt="Image" width="75%" /></div>

Figure 4: Ground track of the ascending and descending halves of orbits 1–15, STK 2D view at 3 Feb 2025 12:40:00 UTCG.

### 2.5 Mission Duration & EOL

The mission lasts five years. This covers several summer bleaching seasons, which is long enough to recognise change between years, and it is a typical design life for a microsatellite. Bleaching is a long-term problem, so a replacement satellite would follow, carrying improved imaging technology. STK simulations were run from 3 Feb 2025 to 3 Feb 2030.

Sun-synchronous orbits are heavily used and already contain a large amount of debris, so the satellite must not be abandoned at the end of its life. International guidelines ask that a satellite in low Earth orbit is removed within 25 years of the end of its mission [14]. Moving it to a graveyard orbit is only practical for geostationary satellites. A controlled de-orbit needs a propulsion system, which ZYZZsat does not have. The EOL plan is therefore passive: a drag sail is deployed at the end of the mission. A drag sail is a thin membrane on deployable booms that increases the area facing the thin upper atmosphere, so that drag lowers the orbit until the satellite burns up on re-entry; it is suitable for low-Earth-orbit altitudes [15].

The loss of altitude per orbit for a circular orbit is Δa = 2π (C_D A / m) ρ a². Table 7 applies this with a drag coefficient C_D of 2.2, a mass of 50 kg, a mean air density ρ of 1 × 10⁻¹³ kg/m³ at 600 km and a density scale height H of about 70 km.

Table 7: Orbital decay with and without the drag sail.

| Case | Area A | Δa per orbit | Decay rate | Lifetime ≈ H / rate |
|---|---|---|---|---|
| Operational, no sail | 0.3 m² | 0.40 m | 2.2 km per year | about 32 years |
| Sail deployed (4 m² sail plus body) | 4.3 m² | 5.8 m | 31 km per year | about 2.2 years |

Without the sail the satellite would stay in orbit for about 32 years, longer than the guideline allows, so the sail is necessary. With a 4 m² sail the satellite re-enters about two years after the end of the mission. Air density at 600 km changes by about a factor of ten over the solar cycle, so the lifetime with the sail could be anywhere from a few months to several years, which is still far inside 25 years. The same calculation shows that during the five-year mission the orbit falls by only about 11 km, which is why no orbit maintenance is needed. The remaining risk is that the sail fails to deploy; a second, independent release mechanism is recommended.

## 3 Conclusion

ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite. A 600 km sun-synchronous orbit at 97.79° inclination gives the same morning lighting on every pass, a 5 m image with a 60 km swath, access to any part of the reef within about five days and a complete overhead map about every 45 days. The Mount Pleasant station sees six passes a day with a mean of 9.7 minutes, and the downlink capacity is 3.5 times the daily data volume. The mission lasts five years without any manoeuvres, and a 4 m² drag sail removes the satellite in about two years, compared with about 32 years without it.

The design has four limitations. First, Vega C has not yet flown, so the Falcon 9 rideshare service is kept as a fallback and the orbit analysis must be repeated if the release altitude differs from 600 km. Second, fluid lensing has only been demonstrated from aircraft at much finer resolution, so its benefit at 5 m from orbit is unproven and the mission relies mainly on direct detection of colour change. Third, Mount Pleasant needs additional S-band and X-band equipment, and the link budget has not been calculated. Fourth, the 45-day complete map is slower than the weekly coverage that reef managers would prefer; a second satellite in the same orbit plane would halve it. With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps that current temperature-based monitoring cannot.

## Bibliography

[1] NOAA, "Ocean acidification," 2020. [Online]. Available: https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification. [Accessed: 10 Nov. 2020].

[2] National Geographic, "Great Barrier Reef coral bleaching map," Aug. 2018. [Online]. Available: https://www.nationalgeographic.com/magazine/2018/08/explore-atlas-great-barrier-reef-coral-bleaching-map-climate-change/. [Accessed: 10 Nov. 2020].

[3] Deepreef Explorer, "Depth model for the Great Barrier Reef (gbr100)." [Online]. Available: https://www.deepreef.org/projects/48-depth-model-gbr.html. [Accessed: 10 Nov. 2020].

[4] Nature, news article on mapping coral bleaching in Hawaii from the air, 2019, doi: 10.1038/d41586-019-02802-2. [Online]. Available: https://www.nature.com/articles/d41586-019-02802-2. [Accessed: 10 Nov. 2020].

[5] V. Chirayath and S. A. Earle, "Drones that see through waves – preliminary results from airborne fluid lensing for centimetre-scale aquatic conservation," *Aquatic Conservation: Marine and Freshwater Ecosystems*, vol. 26, no. S2, pp. 237–250, 2016.

[6] NASA Ames Research Center, "What is fluid lensing?" [Online]. Available: https://www.nasa.gov/feature/ames/what-is-fluid-lensing/. [Accessed: 10 Nov. 2020].

[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds., *Space Mission Engineering: The New SMAD*. Hawthorne, CA, USA: Microcosm Press, 2011.

[8] Arianespace, *Vega User's Manual*, Issue 4, Revision 0, Apr. 2014.

[9] Arianespace, launch kit for Flight VV16, the Small Spacecraft Mission Service (SSMS) proof-of-concept flight, Sep. 2020.

[10] SpaceX, *Rideshare Payload User's Guide*, 2020.

[11] D. A. Vallado, *Fundamentals of Astrodynamics and Applications*, 4th ed. Hawthorne, CA, USA: Microcosm Press, 2013.

[12] European Space Agency, "Types of orbits," 2020. [Online]. Available: https://www.esa.int/Enabling_Support/Space_Transportation/Types_of_orbits. [Accessed: 10 Nov. 2020].

[13] J. E. J. Lovell et al., "The AuScope geodetic VLBI array," *Journal of Geodesy*, vol. 87, pp. 527–538, 2013.

[14] Inter-Agency Space Debris Coordination Committee, *IADC Space Debris Mitigation Guidelines*, IADC-02-01, Revision 2, Mar. 2020.

[15] The Space Review, article 3887 on drag sails for de-orbiting satellites. [Online]. Available: https://www.thespacereview.com/article/3887/1. [Accessed: 10 Nov. 2020].

## Appendix A: STK files and settings

The following STK 11 files are submitted with this report in ZYZZsat_STK.zip.

Table A1: STK files.

| File | Contents |
|---|---|
| ZYZZsat_Mission.sc | Scenario, 3 Feb 2025 00:00:00 to 3 Feb 2030 00:00:00 UTCG |
| ZYZZsat.sa | Satellite, J2 perturbation propagator, elements as in Table 4 |
| Mt_Pleasant_Radio_Observatory.f | Ground facility at 42.8°S, 147.4°E, no elevation constraint |
| Access_ZYZZsat_MtPleasant.csv | Full access report from which Table 5 is taken |
