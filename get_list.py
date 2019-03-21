from requests import get

#list of department pages on spark
cats = ["accounting_fac", "alestle", "anthro_fac", "artanddesign_fac", "bio_fac", "bot", "bulletin", "ce_fac", "chem_fac", "ci_fac", "cmis_fac", "construction_fac", "cs_fac", "dentalmedicine_fac", "digital_collections", "ece_fac", "ef_fac", "el_fac", "english_fac", "fll_fac", "geo_fac", "hcinf_fac", "health_fac", "hist_fac", "iur_pub", "khe_fac", "library_fac", "masscomm_fac", "math_fac", "mie_fac", "mm_fac", "music_fac", "ncerc_pub", "nursing_fac", "pharmacy_fac", "phil_fac", "physics_fac", "polisci_fac", "psych_fac", "publicadmin_fac", "scj_fac", "secd_fac", "segue", "siue_fac", "siueohi", "socialwork_fac", "speech_fac", "stem_annualreports", "stem_briefs", "stem_data", "stem_pres", "stem_pub", "td_fac", "teach_fac", "atcfinal", "dnpprojects", "etd", "artanddesign_walk", "cox", "catalogs", "focus", "ierc_pub", "library_events"]
cats = sorted(cats)

for c in cats:
    i = 1
    t = 0
    b = 0

    while b < 10:
        r = get("https://spark.siue.edu/"+c+"/"+str(i))
        while str(r) != '<Response [404]>':
            i += 1
            t += 1
            r = get("https://spark.siue.edu/"+c+"/"+str(i))
        b += 1
        i += 1
    print(c+", "+str(t))
