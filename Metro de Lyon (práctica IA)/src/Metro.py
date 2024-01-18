import networkx

from Station import Station


class Metro:
    def __init__(self):
        #latitud, longitud y a que linea

        #Linea A
        perrache = Station("Perrache", 45.74849593285, 4.82578449192984, [1] )
        ampere_victor_hugo = Station("Ampère – Victor Hugo", 45.7528990241268, 4.82916820841589, [1] )
        bellecour = Station("Bellecour", 45.7578272339404, 4.8336873209952, [1] )
        cordeliers = Station("Cordeliers", 45.7632413263491, 4.83574324907402, [1] )
        hotel_de_ville_louis_pradel = Station("Hôtel de Ville–Louis Pradel", 45.7673874887601, 4.83628164077502, [1] )
        foch = Station("Foch", 45.768622595485, 4.84422311362784, [1] )
        massena = Station("Masséna", 45.7693297544307, 4.85309636773253, [1] )
        charpennes_charles_hernu = Station("Charpennes – Charles Hernu", 45.7704686872972, 4.8630335488476, [1] )
        republique_villeurbanne = Station("République – Villeurbanne", 45.7705378616497, 4.87363816863047, [1] )
        gratte_ciel = Station("Gratte-Ciel", 45.7690323002035, 4.8824676538264, [1] )
        flachet_alain_gilles = Station("Flachet – Alain Gilles", 45.7675464232399, 4.88989420495417, [1] )
        cusset = Station("Cusset", 45.7656271021859, 4.90023763168677, [1] )
        laurent_bonnevay_astroballe = Station("Laurent Bonnevay – Astroballe", 45.7647844212176, 4.90891542429916, [1] )
        vaulx_en_velin_la_soie = Station("Vaulx-en-Velin – La Soie", 45.7609095875307, 4.92200557938987, [1] )

        #Linea B
        charpennes_charles_hernu = Station("Charpennes – Charles Hernu", 45.7705626837206, 4.8630017998644, [2] )
        brotteaux = Station("Brotteaux", 45.766874905311, 4.85932072875588, [2] )
        gare_part_dieu_vivier_merle = Station("Gare Part-Dieu – Vivier Merle", 45.7615248493848, 4.85780927109367, [2] )
        place_guichard_bourse_du_travail = Station("Place Guichard – Bourse du Travail", 45.7593813852215, 4.84772938639435, [2] )
        saxe_gambetta = Station("Saxe-Gambetta", 45.7538924017277, 4.84704610177028, [2] )
        jean_mace = Station("Jean Macé", 45.7458712481351, 4.84240874211013, [2] )
        place_jean_jaures = Station("Place Jean Jaurès", 45.7380442102733, 4.83753178704279, [2] )
        debourg = Station("Debourg", 45.7313795228594, 4.83365102873608, [2] )
        stade_de_gerland = Station("Stade de Gerland", 45.7270270000004, 4.83080857106596, [2] )
        oullins_gare  = Station("Oullins Gare", 45.766874905311, 4.85932072875588, [2] )

        #Linea C        
        hotel_de_ville_louis_pradel = Station("Hôtel de Ville–Louis Pradel", 45.7674113689742, 4.83631542745492, [3] )
        croix_paquet = Station("Croix-Paquet", 45.7709417551735, 4.83624551950506, [3] )
        croix_rousse = Station("Croix-Rousse", 45.7743021426654, 4.83190175140873, [3] )
        henon = Station("Hénon", 45.7792048953842, 4.82737999981195, [3] )
        cuire = Station("Cuire", 45.7860060248348, 4.83335149986142, [3] )

        #Linea D 
        gare_de_vaise = Station("Gare de Vaise", 45.7807, 4.8047, [4] )
        valmy = Station("Valmy", 45.7746, 4.8056, [4] )
        gorge_de_loup = Station("Gorge de Loup", 45.7668, 4.8052, [4] )
        vieux_lyon_cathedrale_saint_jean = Station("Vieux Lyon – Cathédrale Saint-Jean", 45.7608, 4.8257, [4] )
        bellecour = Station("Bellecour", 45.7585, 4.8337, [4] )
        guillotiere_gabriel_peri = Station("Guillotière – Gabriel Péri", 45.7554, 4.8423, [4] )
        saxe_gambetta = Station("Saxe-Gambetta", 45.7539, 4.847, [4] )
        garibaldi = Station("Garibaldi", 45.7516, 4.854, [4] )
        sans_souci = Station("Sans Souci", 45.7481, 4.8644, [4] )
        monplaisir_lumiere = Station("Monplaisir-Lumière", 45.7455, 4.8725, [4] )
        grange_blanche = Station("Grange Blanche", 45.7429, 4.8789, [4] )
        laennec = Station("Laënnec", 45.7384, 4.8864, [4] )
        mermoz_pinel = Station("Mermoz-Pinel", 45.7309, 4.8873, [4] )
        parilly = Station("Parilly", 45.7196, 4.8876, [4] )
        gare_de_venissieux = Station("Gare de Vénissieux", 45.7052, 4.888, [4] )
   

        self.graph = networkx.Graph()
        #añado los grafos al nodo grande
        self.graph.add_nodes_from([perrache, ampere_victor_hugo, cordeliers, foch, massena, charpennes_charles_hernu,
                                    republique_villeurbanne, gratte_ciel, flachet_alain_gilles, cusset, laurent_bonnevay_astroballe,
                                    vaulx_en_velin_la_soie, brotteaux, gare_part_dieu_vivier_merle, place_guichard_bourse_du_travail,
                                    saxe_gambetta, jean_mace, place_jean_jaures, debourg, stade_de_gerland, oullins_gare,
                                    hotel_de_ville_louis_pradel, croix_paquet, croix_rousse, henon, cuire, gare_de_vaise, valmy,
                                    gorge_de_loup, vieux_lyon_cathedrale_saint_jean, bellecour, guillotiere_gabriel_peri, garibaldi,
                                    sans_souci, monplaisir_lumiere, grange_blanche, laennec, mermoz_pinel, parilly, gare_de_venissieux
  
                                   ])
        
        #El primer hueco es tiempo, el segundo la distancia
        self.graph.add_weighted_edges_from([ #Linea A
                                            (perrache, ampere_victor_hugo, [1, 0.4]), (ampere_victor_hugo, bellecour, [1, 0.6]), (bellecour, cordeliers, [2, 0.7]),
                                            (cordeliers, hotel_de_ville_louis_pradel, [2, 0.4]), (hotel_de_ville_louis_pradel, foch, [2, 0.7]), (foch, massena, [1, 0.7]),
                                            (massena, charpennes_charles_hernu, [2, 0.8]), (charpennes_charles_hernu, republique_villeurbanne, [1, 0.8]),
                                            (republique_villeurbanne, gratte_ciel, [2, 0.7]), (gratte_ciel, flachet_alain_gilles, [1, 0.6]), (flachet_alain_gilles, cusset, [2, 0.9]),
                                            (cusset, laurent_bonnevay_astroballe, [2, 0.6]), (laurent_bonnevay_astroballe, vaulx_en_velin_la_soie, [1, 1.1]),
                                            #Linea B
                                            (charpennes_charles_hernu, brotteaux, [1, 0.5]), (brotteaux, gare_part_dieu_vivier_merle, [2, 0.6]), (gare_part_dieu_vivier_merle, place_guichard_bourse_du_travail, [2, 0.9]),
                                            (place_guichard_bourse_du_travail, saxe_gambetta, [2, 0.6]), (saxe_gambetta, jean_mace, [2, 1.1]), (jean_mace, place_jean_jaures, [2, 0.9]), (place_jean_jaures, debourg, [1, 0.8]),
                                            (debourg, stade_de_gerland, [3, 0.5]), (stade_de_gerland, oullins_gare, [4, 1.7]), 
                                            #Linea C
                                            (hotel_de_ville_louis_pradel, croix_paquet, [2, 0.4]), (croix_paquet, croix_rousse, [2, 0.5]), (croix_rousse, henon, [2, 0.7]), (henon, cuire, [2, 0.8]),
                                            #Linea D
                                            (gare_de_vaise, valmy, [2, 0.7]), (valmy, gorge_de_loup, [2, 0.9]), (gorge_de_loup, vieux_lyon_cathedrale_saint_jean, [2, 1.7]), (vieux_lyon_cathedrale_saint_jean, bellecour, [1, 0.6]),
                                            (bellecour, guillotiere_gabriel_peri, [2, 0.8]), (guillotiere_gabriel_peri, saxe_gambetta, [1, 0.4]), (saxe_gambetta, garibaldi, [1, 0.6]),
                                            (garibaldi, sans_souci, [2, 1.0]), (sans_souci, monplaisir_lumiere, [1, 0.5]), (monplaisir_lumiere, grange_blanche, [2, 0.6]), (grange_blanche, laennec, [1, 0.8]),
                                            (laennec, mermoz_pinel, [2, 0.9]), (mermoz_pinel, parilly, [2, 1.2]), (parilly, gare_de_venissieux, [2, 1.6])])
        
        self.map = {"Perrache": perrache, "Ampère – Victor Hugo":ampere_victor_hugo, "Cordeliers": cordeliers,
                    "Foch":foch, "Masséna":massena,"Charpennes – Charles Hernu":charpennes_charles_hernu,
                    "République – Villeurbanne":republique_villeurbanne, "Gratte-Ciel":gratte_ciel,
                    "Flachet – Alain Gilles": flachet_alain_gilles, "Cusset": cusset, "Laurent Bonnevay – Astroballe": laurent_bonnevay_astroballe, 
                    "Vaulx-en-Velin – La Soie":vaulx_en_velin_la_soie,"Brotteaux":brotteaux, "Gare Part-Dieu – Vivier Merle":gare_part_dieu_vivier_merle, 
                    "Place Guichard – Bourse du Travail":place_guichard_bourse_du_travail, "Saxe-Gambetta":saxe_gambetta,"Jean Macé": jean_mace, 
                    "Place Jean Jaurès": place_jean_jaures, "Debourg":debourg, "Stade de Gerland":stade_de_gerland, "Oullins Gare":oullins_gare, 
                    "Hôtel de Ville–Louis Pradel": hotel_de_ville_louis_pradel,"Croix-Paquet": croix_paquet, "Croix-Rousse": croix_rousse, "Hénon": henon, 
                    "Cuire": cuire, "Gare de Vaise":gare_de_vaise, "Valmy": valmy, "Gorge de Loup":gorge_de_loup, 
                    "Vieux Lyon – Cathédrale Saint-Jean":vieux_lyon_cathedrale_saint_jean,"Bellecour":bellecour, 
                    "Guillotière – Gabriel Péri":guillotiere_gabriel_peri, "Garibaldi":garibaldi, "Sans Souci":sans_souci, 
                    "Monplaisir-Lumière":monplaisir_lumiere, "Grange Blanche":grange_blanche, "Laënnec":laennec, 
                    "Mermoz-Pinel":mermoz_pinel,"Parilly":parilly, "Gare de Vénissieux": gare_de_venissieux                    
                     }
