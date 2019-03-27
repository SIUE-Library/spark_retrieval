from requests import get
import re

#list of department pages on spark
cats = ["accounting_fac", "anthro_fac", "artanddesign_fac", "bio_fac", "bot", "bulletin", "ce_fac", "chem_fac", "ci_fac", "cmis_fac", "construction_fac", "cs_fac", "dentalmedicine_fac", "digital_collections", "ece_fac", "ef_fac", "el_fac", "english_fac", "fll_fac", "geo_fac", "hcinf_fac", "health_fac", "hist_fac", "iur_pub", "khe_fac", "library_fac", "masscomm_fac", "math_fac", "mie_fac", "mm_fac", "music_fac", "ncerc_pub", "nursing_fac", "pharmacy_fac", "phil_fac", "physics_fac", "polisci_fac", "psych_fac", "publicadmin_fac", "scj_fac", "secd_fac", "segue", "siue_fac", "siueohi", "socialwork_fac", "speech_fac", "stem_annualreports", "stem_briefs", "stem_data", "stem_pres", "stem_pub", "td_fac", "teach_fac"]

cats = sorted(cats)

for c in cats:
    n = 1
    r = get("https://spark.siue.edu/"+c+"/index.html")
    while str(r) != '<Response [404]>':
'''
        #match all links in r
        link = r'<a href="https:\/\/spark\.siue\.edu\/.{1,41}\d{1,4}"'
        m = re.findall(link, r.text, re.I|re.M)
        for line in m:
            if len(re.findall(r'index.\d?.?html', line)) == 0:

                t = get(str(line)[9:-1]).text
                p = re.findall(r'>.{10,150}<\/p>', t)[0][1:-4]

                p = p.replace('" by', ' by')
                print(c+"\t"+str(p))

        n+=1
        r = get("https://spark.siue.edu/"+c+"/index."+str(n)+".html")
'''
