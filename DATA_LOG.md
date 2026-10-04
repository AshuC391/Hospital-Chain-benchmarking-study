# Data log

## Collection
FY26 (year ended 31 March 2026) results of six listed chains, taken from company releases and earnings calls and press summaries of them. Each row in `data/peer_data.csv` carries its source.

## Cleaning and judgement calls
1. **Fortis ARPOB:** reported as Rs 2.51 Cr per bed per year; converted to per day (2.51 x 10^7 / 365 = Rs 68,767).
2. **Max ARPOB:** the four quarterly figures (Rs 78.0k, 77.3k, 77.9k, 77.9k) were averaged to approximate the full year.
3. **Apollo ARPOB rejected:** a figure of about Rs 187,000 that circulates in summaries is revenue per patient, not per occupied bed per day. It was not used.
4. **Yatharth Hospital figures rejected:** a filing in the search results belonged to a different company and was excluded.
5. **Not disclosed:** Narayana occupancy, Apollo ARPOB, Fortis and Medanta full-year ALOS are left blank rather than estimated.
6. **Scope of driver split:** only chains with both ARPOB and occupancy (Max, Fortis, Medanta, KIMS).
7. **Margin definitions** were kept as each company reports them and flagged as not strictly comparable.
