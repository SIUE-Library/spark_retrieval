from requests import get
import re

#list of department pages on spark
cats = ["accounting_fac", "anthro_fac", "artanddesign_fac", "bio_fac", "ce_fac", "chem_fac", "ci_fac", "cmis_fac", "construction_fac", "cs_fac", "dentalmedicine_fac", "ece_fac", "ef_fac", "el_fac", "english_fac", "fll_fac", "geo_fac", "hcinf_fac", "health_fac", "hist_fac", "iur_pub", "khe_fac", "library_fac", "masscomm_fac", "math_fac", "mie_fac", "mm_fac", "music_fac", "ncerc_pub", "nursing_fac", "pharmacy_fac", "phil_fac", "physics_fac", "polisci_fac", "psych_fac", "publicadmin_fac", "scj_fac", "secd_fac", "siue_fac", "siueohi", "socialwork_fac", "speech_fac", "stem_briefs", "stem_data", "stem_pres", "stem_pub", "td_fac", "teach_fac"]

cats = sorted(cats)

deptMap = []

for c in cats:
    n = 1
    r = get("https://spark.siue.edu/"+c+"/index.html")
    while str(r) != '<Response [404]>':
        t = ""
        #match all links in r
        link = r'<a href="https:\/\/spark\.siue\.edu\/.{1,150}\d{1,4}".{1,200}<\/a>, .{10,100}<\/p>'
        m = re.findall(link, r.text, re.I|re.M)


        if c == "siue_fac":
            #go deeper and check the dept
            for line in m:
                temp = re.findall(r'<a href=".{1,41}\d{1,4}" >', line)

                if len(temp) > 0:
                    temp = t
                    t = get(str(line)[9:].split('" >')[0])
                    p = re.findall(r'<h4>Department<\/h4>\n<p>.{1,55}<\/p>', t.text)
                    if len(p) > 0:
                        p = p[0]
                        p = str(p[23:-4])
                        #map p to bept code?
                        print(t.url + "\t"+c+"\t"+line.split('" >')[1].replace("</p>", "").replace("</a>", "")+"\t"+p)

                    elif "siue_fac" in t.url:
                        print(t.url + "\t"+c+"\t"+line.split('" >')[1].replace("</p>", "").replace("</a>", "")+"\tNo Dept Detected")
                    else:
                        print(t.url + "\t"+c+"\t"+line.split('" >')[1].replace("</p>", "").replace("</a>", "")+"\t"+t.url.split("/")[3])

        else:
            for l in m:
                print(r.url + "\t"+c+"\t"+l.split('" >')[1].replace("</p>", "").replace("</a>", "")+"\t")

        n+=1

        r = get("https://spark.siue.edu/"+c+"/index."+str(n)+".html")
