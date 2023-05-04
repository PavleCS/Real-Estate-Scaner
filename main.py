from Nekretnine import Nekretnine
from Maps import Maps
from Form import Form

nekretnine = Nekretnine()
sva_sela = nekretnine.sva_sela
sve_cene = nekretnine.sve_cene
sve_povrsine = nekretnine.sve_povrsine
svi_linkovi = nekretnine.svi_linkovi


maps = Maps()
for selo in sva_sela:
    maps.get_map_info(selo)


sve_distance = maps.results


form = Form()


for n in range(len(sva_sela)):
    try:
        dist_ljub = sve_distance[sva_sela[n]][0]["Ljubljana"]
        dist_mar = sve_distance[sva_sela[n]][1]["Maribor"]
        form.fill_form(sva_sela[n], sve_cene[n], sve_povrsine[n], svi_linkovi[n], dist_ljub, dist_mar)
    except IndexError:
        print("Index error skipped")