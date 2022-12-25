#Art-tekstien lisämoduuli
import pyfiglet

#Pääfunktio
def Osio1():
    #Otsikko, art-teksti
    T = "Cisco CheatSheet"
    ASCII_art = pyfiglet.figlet_format(T)
    print(ASCII_art, "© Oskari Heinonen")

    #Esittelyteksti
    print("\nHei!\n")
    print("Tämä ohjelma sisältää rautalankamalleja Ciscon reitittimien ja kytkimien erilaisiin komentorivipohjaisiin konfigurointeihin.")
    print("Ohjelmassa esitetyt konfigurointitavat ovat vain yksinkertaisia esimerkkejä, eivätkä ne välttämättä ole ainoita oikeita tapoja konfiguroida.")
    print("Soveltavammissa tilanteissa komentoihin löydät apua laitteiden komentorivillä kysymysmerkin (?) avulla.")
    print("Tässä ohjelmassa komennot ovat esitetty aaltoviivojen sisällä muodossa ~komento~.")
    
    while True:

        #Päävalikko
        print("\nMitä haluat tehdä?")
        print("1 - Poistaa vanhoja konfiguraatioita")
        print("2 - Ensimmäiset toimenpiteet kytkimelle/reitittimelle")
        print("3 - Konfiguroida reitittimen liitäntöjä (IPv4)")
        print("4 - Asettaa kytkimelle hallinta- ja oletusyhdyskäytäväosoitteen (IPv4)")
        print("5 - Konfiguroida VLAN-verkkoja")
        print("6 - Konfiguroida kytkinten välille EtherChannel")
        print("7 - Konfiguroida reitittimeen staattisia-, oletus- tai host-reittejä")
        print("8 - Konfiguroida reitittimeen OSPFv2")
        print("9 - Konfiguroida reitittimeen DHCPv4")
        print("10 - Konfiguroida reitittimeen NAT")
        print("11 - Asettaa kytkimelle/reitittimelle ensimmäiset turvallisuusmääritykset")
        print("12 - Konfiguroida kytkimeen/reitittimeen SSH-yhteys")
        print("13 - Konfiguroida kytkimeen muita turvallisuusmäärityksiä")
        print("14 - Lopettaa ohjelman")
        syote = input("Valitse toiminto 1-14 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 15):

                #Tähän if-ehtoihin eri päävalikon funktiot
                if koklukusyote == 1:
                    print("\n")
                    Osio2()
                elif koklukusyote == 2:
                    print("\n")
                    Osio3()
                elif koklukusyote == 3:
                    print("\n")
                    Osio4()
                elif koklukusyote == 4:
                    print("\n")
                    Osio5()
                elif koklukusyote == 5:
                    print("\n")
                    Osio6()
                elif koklukusyote == 6:
                    print("\n")
                    Osio7()
                elif koklukusyote == 7:
                    print("\n")
                    Osio8()
                elif koklukusyote == 8:
                    print("\n")
                    Osio9()
                elif koklukusyote == 9:
                    print("\n")
                    Osio10()
                elif koklukusyote == 10:
                    print("\n")
                    Osio11()
                elif koklukusyote == 11:
                    print("\n")
                    Osio12()
                elif koklukusyote == 12:
                    print("\n")
                    Osio13()
                elif koklukusyote == 13:
                    print("\n")
                    Osio14()
                elif koklukusyote == 14:
                    print("Lopetit ohjelman.")
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-14. Valitse jokin toiminto väliltä 1-14.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-14.")


def Osio2():
    #Osio 2 ajaa vaihtoehdon 1 eli miten poistetaan vanhat konfiguraatiot
    print("Reitittimestä ja kytkimestä olisi aina konfiguroinnin alkuun hyvä tarkistaa, onko sinne jäänyt sellaisia määrityksiä, joita sinne ei toivota.")
    print("Tätä varten molemmista olisi kannattavaa tarkistaa vähintään runconfig ~show running-config~, sekä reitittimestä reititystaulu ~show ip route~, ja kytkimestä VLAN-määritykset ~show vlan brief~.")

    while True:

        print("\nMitä haluat tehdä?\n1 - Poistaa vain yksittäisiä ei-haluttuja komentoja\n2 - Poistaa running-configin\n3 - Poistaa startup-configin\n4 - Palata päävalikkoon")
        syote = input("Valitse toiminto 1-4 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 5):

                if koklukusyote == 1:
                    print("\nMikäli laitteessa on vain yksittäisiä ei-haluttuja komentoja, ne kannattaa poistaa avainsanalla ~no~. Annat siis sen komennon uudestaan, jonka haluat poistaa, ja lisäät vain sen eteen avainsanan ~no~.")
                    print("Näin ollen et poista kaikkia konfigurointeja turhaan.")
    
                elif koklukusyote == 2:
                    print("\nMikäli haluat poistaa running-configin, anna komento ~reload~, joka käynnistää laitteen uudelleen. Tiedot, joita ei ole siirretty startup-configiin, katoaa.")
                    print("Jos olet konfiguroinut VLAN-verkkoja, ne täytyy poistaa vielä erikseen komennolla ~delete flash:vlan.dat~.")

                elif koklukusyote == 3:
                    print("\nMikäli haluat poistaa startup-configin eli pysyväismuistin, anna komento ~write erase~ tai ~erase startup-config~." )
                    print("Jos olet konfiguroinut VLAN-verkkoja, ne täytyy poistaa vielä erikseen komennolla ~delete flash:vlan.dat~.")

                elif koklukusyote == 4:
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-4. Valitse jokin toiminto väliltä 1-4.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-4.")


def Osio3():
    #Osio 3 ajaa vaihtoehdon 2 eli ensimmäiset toimenpiteet reitittimelle/kytkimelle
    print("Suositeltavaa on, että konfiguroimattomat verkkolaitteet nimetään heti ensimmäisenä. Tällä tavoin virheiden määrä vähenee, kun laitteet pystyy erottamaan toisistaan kuvaavan nimen perusteella.")
    print("Nimeäminen tapahtuu komennolla ~hostname~, jonka perään kirjoitetaan itse valittu, kuvaileva nimi.")
    print("\nToinen hyvä käytäntö on komennon ~logging synchronous~ antaminen konsoli- ja/tai vty-linjoille. Tämä estää sen, että laitteiden ilmoitukset keskeyttäisivät komentojen kirjoittelua.")
    print("Konsoliliitäntä tarkoittaa yhteyttä kaapelin välityksellä, kun taas vty-liitäntä etäyhteyttä SSH:n tai Telnetin välityksellä.")
    print("Em. komento annetaan siis kytkimeen liitännässä ~line console 0~ tai ~line vty 0 15~, ja reitittimeen liitännässä ~line console 0~ tai ~line vty 0 4~")


def Osio4():
    #Osio 4 ajaa vaihtoehdon 3 eli miten konfiguroidaan IPv4-liitäntöjä
    print("Reitittimen liitäntöihin konfiguroidaan IP-osoite, ja niille voidaan antaa myös kuvaus. Esimerkiksi reititin 1:ltä lähtevä liitäntä kohti reititin 2:ta voidaan kuvailla 'liitäntä kohti reititin 2:ta'.")
    print("\nValitaan ensin liitäntä komennolla ~interface [fastEthernet / gigabitEthernet / serial] X/X~.")
    print("Sen jälkeen annetaan IP-osoite ja sen aliverkon maski komennolla ~ip address X.X.X.X Y.Y.Y.Y~.")
    print("Voit myös antaa vapaavalintaisen kuvauksen liitännälle, joka annetaan aloittamalla komento avainsanalla ~description~, ja sen perään voi kirjoittaa haluamallaan tavalla linkille kuvauksen.")
    print("Liitäntä täytyy usein myös avata komennolla ~no shutdown~.")


def Osio5():
    #Osio 5 ajaa vaihtoehdon 4 eli miten konfiguroidaan kytkimelle hallinta- ja DGW-osoite
    print("Kytkimelle määritetään hallintaosoite, kun siihen halutaan saada etäyhteys esimerkiksi satojen kilometrien päästä, jolloin siihen ei ole mahdollista päästä suoraan kaapelin kautta kiinni.")
    print("Etäyhteys tapahtuu SSH- tai Telnet-yhteyden avulla. SSH on suojauksensa vuoksi suositeltavampi tapa.")
    print("Hallintaosoite määritetään hallinta-/native-VLAN:iin. Jos hallinta-VLAN:a ei ole erikseen määritelty, määritetään osoite VLAN:iin 1.")
    print("\nEnsin määritetään liitäntä, johon osoite lisätään. Tämä on siis joko VLAN 1 (eli oletus) tai jokin toinen erikseen määritelty hallinta-VLAN. Annetaan siis komento ~interface vlan X~.")
    print("Sen jälkeen annetaan IP-osoite ja sen aliverkon maski komennolla ~ip address X.X.X.X Y.Y.Y.Y~.")
    print("Liitäntä voidaan myös joutua avaamaan komennolla ~no shutdown~.")
    print("Lopuksi palaa vielä komennolla ~exit~ 'config'-tilaan, ja anna kytkimelle oletusyhdyskäytävän osoite komennolla ~ip default-gateway X.X.X.X~.")


def Osio6():
    #Osio 6 ajaa vaihtoehdon 5 eli miten konfiguroidaan VLAN

    #3D-otsikko
    T = "VLAN"
    ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
    print(ASCII_art_1)

    print("\nVLAN-verkot ovat tehokas keino yhdistää eri laitteita toisiinsa asettamalla ne samaan virtuaaliseen lähiverkkoon eli VLAN:iin. Tällöin ne käyttäytyvät kuin olisivat samassa fyysisessä lähiverkossa.")
    print("VLAN:ien avulla voidaan segmentoida esimerkiksi ison organisaation verkko pienempiin osiin, kuten henkilöstö- ja taloushallinnolle omat virtuaaliset lähiverkkonsa.")
    print("Tällöin myös broadcast-alueet pienenevät ja verkon suorituskyky kasvaa.")
    print("Liikenne eri VLAN:ien välillä kulkee trunk-linkkien kautta. Lisäksi on kaksi tapaa toteuttaa VLAN-konfiguraatio, Router-on-a-stick tai MLS (MultiLayerSwitching).")
    print("Router-on-a-stick toteutetaan, kun virtuaalisista lähiverkoista ulospäin reitittävä laite on reititin. MLS taas toteutetaan, kun kyseinen laite on monikerroskytkin eli reitittävä kytkin.")

    while True:

        print("\nMitä haluat tehdä?\n1 - Muodostaa ja nimetä VLAN:n sekä liittää sen tiettyihin kytkimen portteihin\n2 - Konfiguroida trunk-portteja\n3 - Konfiguroida DTP\n4 - Router-on-a-stick-konfigurointi\n5 - MLS-konfigurointi\n6 - Palata päävalikkoon")
        syote = input("Valitse toiminto 1-6 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 7):

                if koklukusyote == 1:
                    print("\nUusi VLAN muodostetaan antamalla komentona sen numero väliltä 2-1001 ja max 32-merkkinen nimi. Anna siis komennot ~vlan X~ ja ~name X~.")
                    print("\nVLAN:t tulee liittää tiettyihin kytkimen portteihin, koska kun tietokone liitetään näihin portteihin, se on automaattisesti tietyssä VLAN:ssa. Tämän myötä tietokoneen IP-osoite ja oletusyhdyskäytävän osoite tulee myös vaihtaa VLAN:n mukaiseksi.")
                    print("Valitse siis ensin liitäntä/liitännät, joihin haluat liittää VLAN:n (~interface [fastEthernet / gigabitEthernet] X/X~), aseta se access-tilaan komennolla ~switchport mode access~, ja kerro liitännälle mihin VLAN:iin se kuuluu komennolla ~switchport access vlan X~.")
                    print("\nJos haluat konfiguroida IP-puhelimille oman VLAN:n, tarvitset nimeämisen ja access-tilan määrityksen lisäksi pari lisäkomentoa.")
                    print("Siirry siis siihen liitäntään, johon liität IP-puhelimen VLAN:n (~interface [fastEthernet / gigabitEthernet] X/X~), ja anna komennot ~switchport mode access~, ~mls qos trust cos~ ja ~switchport voice vlan X~.")

                elif koklukusyote == 2:
                    print("\nTrunk-linkit konfiguroidaan ottamalla tietyt portit trunk-käyttöön, esimerkiksi useampi portti samanaikaisesti komennolla ~interface range [fastEthernet / gigabitEthernet] X/X-Y~.")
                    print("Monikerroskytkimille täytyy antaa ensin komento ~switchport trunk encapsulation dot1q~, jonka jälkeen asetetaan liitäntä/liitännät trunk-tilaan komennolla ~switchport mode trunk~. Layer 2-kytkimille riittää vain jälkimmäinen.")
                    print("Pysytään edelleen trunk-porttien konfiguroinnissa ja annetaan vielä komento ~switchport trunk native vlan X~. Tällä eritellään hallinta-VLAN muista.")

                elif koklukusyote == 3:
                    print("\nDTP (Dynamic Trunking Protocol) asetetaan tietyille kytkimen porteille päälle, mikäli halutaan portin aktiivisesti pyrkivän muuttamaan yhteyttä trunk-yhteydeksi.")
                    print("\nDTP:n saa päälle siirtymällä haluamaansa liitäntään (~interface [fastEthernet / gigabitEthernet] X/X~), ja antamalla komennon ~switchport mode dynamic desirable~.")
                    print("DTP:n saa pois päältä siirtymällä jälleen tiettyyn liitäntään (~interface [fastEthernet / gigabitEthernet] X/X~), ja antamalla komennot ~switchport mode trunk~ ja ~switchport nonegotiate~.")

                elif koklukusyote == 4:
                    print("\nRouter-on-a-stick-menetelmässä muodostetaan ja nimetään ensin VLAN:t, määritetään ne tiettyihin kytkimen portteihin sekä konfiguroidaan hallintaliitäntä ja trunk-portit (kts. edelliset kohdat).\n")
                    print("Nyt, kun reitittävänä laitteena on reititin, tarvitsee reitittimeen konfiguroida VLAN-verkkojen aliliitännät. Esimerkiksi VLAN 10 voitaisiin selkeyden vuoksi määritellä aliliitäntään 0/0.10.")
                    print("Siirrytään siis aliliitäntään komennolla ~interface [fastEthernet / gigabitEthernet] X/X.YY~, johon kerrotaan mihin VLAN:iin se liittyy komennolla ~encapsulation dot1q X~ ja sen IP-osoitteeksi oletusyhdyskäytävän osoite komennolla ~ip address X.X.X.X Y.Y.Y.Y~.")
                    print("Erityishuomiona edelliseen, anna seuraava komento, mikäli kyseessä oleva VLAN on hallinta-VLAN eli native-VLAN: ~encapsulation dot1q X native~.")
                    print("\nKun olet saanut kaikki aliliitännät konfiguroitua, siirry 'pääliitäntään' ja avaa se komennolla ~no shutdown~. Tällä tavoin liikenne pääsee kulkemaan VLAN-verkkoihin.")
                    print("Aliliitännällä tarkoitetaan siis esimerkiksi fastEthernet 0/0.10:ä, kun taas pääliitännällä fastEthernet 0/1:tä, joka pitää sisällää kaikki aliliitännät.")

                elif koklukusyote == 5:
                    print("\nMLS-menetelmässä muodostetaan ja nimetään ensin VLAN:t, määritetään ne tiettyihin kytkimen portteihin sekä konfiguroidaan hallintaliitäntä ja trunk-portit (kts. edelliset kohdat).")
                    print("\nNyt, kun reitittävänä laitteena on monikerroskytkin, sille täytyy muodostaa VLAN-liitännät ja antaa niille IP-osoitteet komennoilla ~interface vlan X~ ja ~ip address X.X.X.X Y.Y.Y.Y~. IP-osoite on VLAN:n oletusyhdyskäytävän osoite.")
                    print("Myös reitittävä portti eli monikerroskytkimestä ulkoverkon suuntaan oleva portti täytyy konfiguroida.")
                    print("Siirry siis reitittävään porttiin komennolla ~interface [fastEthernet / gigabitEthernet] X/X~, ja anna komennot ~no switchport~ ja ~ip address X.X.X.X Y.Y.Y.Y~. IP-osoitteeksi portin osoite. Muista avata portti komennolla ~no shutdown~.")
                    print("Lopuksi anna monikerroskytkimelle 'config'-tilassa komento ~ip routing~, joka sallii monikerroskytkimen IP-reitityksen.")

                elif koklukusyote == 6:
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-6. Valitse jokin toiminto väliltä 1-6.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-6.")


def Osio7():
    #Osio 7 ajaa vaihtoehdon 6 eli miten konfiguroidaan EtherChannel
    print("Kaikki portit, joista EtherChannel halutaan muodostaa, täytyy konfiguroida ensin staattisiksi trunk-porteiksi (kts. päävalikko osio 5 ja sieltä trunk-porttien konfigurointi).")
    print("\nSiirry ensin liitäntöihin, joista haluat muodostaa EtherChannelin, komennolla ~interface range [fastEthernet / gigabitEthernet] X/X-Y~. Tämän jälkeen sulje heti liitännät komennolla ~no shutdown~.")
    print("Suljettuihin liitäntöihin muodostetaan porttikanavaliitäntä, ja sille voidaan valita numeroksi esimerkiksi 1. Komentoa jatketaan siten, että sille valitaan vielä EtherChannel-tila.")
    print("EtherChannel-tila voi olla joko LACP-protokollan mukaisesti 'active' tai 'passive', tai PAgP-protokollan mukaisesti 'desirable' tai 'auto'. Se voi olla myös 'on'. Tilat määrittelevät sen, miten portit yrittävät muodostaa EtherChannel-ryhmittymiä.")
    print("EtherChannel-tilat täytyy kuitenkin konfiguroida saman protokollan mukaisesti kytkinten välillä, esim. desirable <--> desirable, desirable <--> auto ym.")
    print("Porttikanavaliitäntä muodostetaan siis komennolla ~channel-group X mode Y~. Tämän jälkeen avataan liitännät komennolla ~no shutdown~.")
    print("\nSeuraavaksi palataan 'config'-tilaan, ja sieltä siirrytään konfiguroimaan juuri luotua porttikanavaa komennolla ~interface port-channel X~.")
    print("Porttikanavaliitännälle täytyy vielä kertoa native-VLAN sekä mitkä VLAN:t ovat sallittuja kulkemaan sen sisällä. Nämä tapahtuu komennoilla ~switchport trunk native vlan X~ ja ~switchport trunk allowed vlan X,Y,Z~.")


def Osio8():
    #Osio 8 ajaa vaihtoehdon 7 eli miten konfiguroidaan reittejä
    print("Staattisia reittejä määritetään reitittimeen, koska reitittimet tuntevat vain omat suoraan kytketyt verkkonsa, eivätkä tiedä seuraavan reitittimen takana olevista verkoista mitään.")
    print("Staattiset reitit ovat vaihtoehto OSPF:n kaltaiselle dynaamiselle reititykselle. Molemmissa on omat tarkoitusperänsä.\n")
    print("Oletusreittejä käytetään, jotta voidaan muodostaa reitti, joka täsmää kaikkien verkossa kulkevien pakettien kanssa. Niitä käytetään yleensä 'reunareitittimen' ja ISP-reitittimen välillä.\n")
    print("Host-reittejä käytetään, kun halutaan reitti suoraan tietylle host-laitteelle.")

    while True:

        print("\nMitä haluat tehdä?\n1 - Konfiguroida staattisia reittejä\n2 - Konfiguroida oletusreittejä\n3 - Konfiguroida host-reittejä\n4 - Palata päävalikkoon")
        syote = input("Valitse toiminto 1-4 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 5):

                if koklukusyote == 1:
                    print("\nReitittimelle täytyy kertoa staattisia reittejä määriteltäessä tuntemattoman verkon IP-osoite, sen aliverkon maski, ja seuraavan reitittimen next-hop-liitännän osoite, eli se, johon paketti matkalla tähän verkkoon ensimmäisenä 'törmää'.")
                    print("'Törmäysportin' sijaan voi antaa myös exit-liitännän, eli sen liitännän, josta paketti lähtee kohti tuntematonta verkkoa, esimerkiksi gigabitEthernet 0/1.")
                    print("Komento on siis ~ip route X.X.X.X Y.Y.Y.Y Z.Z.Z.Z~ tai ~ip route X.X.X.X Y.Y.Y.Y [fastEthernet / gigabitEthernet / serial] X/X~.")
    
                elif koklukusyote == 2:
                    print("\nOletusreitti on 'nollareitti' eli verkon osoite ja sen aliverkon maski on pelkkiä nollia. Viimeiseksi annetaan staattisen reitin tavoin 'törmäysportti' tai exit-liitäntä.")
                    print("Komento on siis: ~ip route 0.0.0.0 0.0.0.0 X.X.X.X~ tai ~ip route 0.0.0.0 0.0.0.0 [fastEthernet / gigabitEthernet / serial] X/X~.")

                elif koklukusyote == 3:
                    print("\nHost-reittiä määriteltäessä reitittimelle kerrotaan kohdelaitteen IP-osoite, täysi /32 aliverkon maski, sekä 'törmäysportin' IP-osoite tai exit-liitäntä.")
                    print("Komento on siis: ~ip route X.X.X.X 255.255.255.255 Y.Y.Y.Y~ tai ~ip route X.X.X.X 255.255.255.255 [fastEthernet / gigabitEthernet / serial] X/X~.")

                elif koklukusyote == 4:
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-4. Valitse jokin toiminto väliltä 1-4.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-4.")


def Osio9():
    #Osio 9 ajaa vaihtoehdon 8 eli miten konfiguroidaan OSPFv2

    #3D-otsikko
    T = "OSPF"
    ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
    print(ASCII_art_1)

    print("\nAloita valitsemalla OSPF-prosessinumero. Se voi olla mikä vain väliltä 1-65535, tärkeintä on, että se on sama kaikilla alueen OSPF-reitittimillä. Tämän jälkeen anna komento valitsemallasi numerolla: ~router ospf X~.")
    print("Reititin siirtyy OSPF-konfigurointitilaan. Seuraavaksi anna kaikille OSPF-reitittimille router id, joka on IPv4-osoitteen kaltainen ja sen tarkoitus on yksilöidä OSPF-reitittimet. Komento on: ~router-id X.X.X.X~.")
    print("Mikäli router id:tä ei anna erikseen, router id muodostuu reitittimen joko korkeimman loopback- tai fyysisen osoitteensa mukaan.\n")

    print("Jokaisen OSPF-reitittimen tulisi mainostaa omia verkkojaan, eli niitä verkkoja, jotka ovat suoraan yhteydessä siihen.")
    print("Tämä onnistuu komennolla ~network X.X.X.X W.W.W.W area 0~, jossa siis kerrotaan oman verkon osoite, sen villikorttimaski sekä area id, jonka suositellaan olevan 0.")
    print("Villikorttimaski on päinvastainen versio aliverkon maskista, eli mikäli kyseisen oman verkon aliverkon maski olisi esimerkiksi 255.255.255.0, sen villikorttimaski on 0.0.0.255, tai 255.255.192.0 <--> 0.0.63.255.\n")

    print("Oletuksena kaikki reitittimen liitännät kannattaa asettaa passiivisiksi OSPF-liitännöiksi, ja avata vain tarvittavat. Tämä siksi, koska turhat aktiiviset OSPF-liitännät kuormittavat verkkoa.")
    print("Aktiivisiksi liitännöiksi tarvitaan sellaiset, jotka yhdistyvät seuraavaan OSPF-reitittimeen.")
    print("Passivoi siis ensimmäisenä kaikki liitännät komennolla ~passive-interface default~, jonka jälkeen aktivoi tarvittavat liitännät komennolla ~no passive-interface [fastEthernet / gigabitEthernet / serial] X/X~.\n")

    print("Edellisten lisäksi ASBR-reititin (autonomous system boundary router) eli internetiin yhteydessä oleva 'reunareititin' täytyy konfiguroida oletusreitin tietojen lähteeksi, jolloin se levittää oletusreitin tietoja OSPF-päivityksissä muille reitittimille.")
    print("ASBR-reitittimeen siis konfiguroidaan oletusreitti, joka osoittaa internetin suuntaan (kts. tarvittaessa osio 6), sekä annetaan seuraavat komennot: ~router ospf X~ ja ~default-information originate~.")


def Osio10():
    #Osio 10 ajaa vaihtoehdon 9 eli miten konfiguroidaan DHCPv4

    #3D-otsikko
    T = "DHCP"
    ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
    print(ASCII_art_1)

    print("\nTässä osiossa käsitellään DHCPv4:n konfigurointia.")
    print("Vaihtoehtoina ovat reitittimen konfigurointi toimimaan DHCPv4-palvelimena eli halutaan sen jakavan verkon host-laitteille osoitteita, ulkopuolisen DHCPv4-palvelimen käyttöönotto tai reitittimen konfigurointi DHCPv4-client-laitteeksi.\n")

    while True:

        print("\nMitä haluat tehdä?\n1 - Konfiguroida reititin DHCPv4-palvelimeksi\n2 - Ottaa oman verkon ulkopuolisen DHCPv4-palvelimen käyttöön\n3 - Konfiguroida reititin DHCPv4-client-laitteeksi\n4 - Palata päävalikkoon")
        syote = input("Valitse toiminto 1-4 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 5):

                if koklukusyote == 1:
                    print("\nHaluat siis, että reitittimesi jakaa verkkosi host-laitteille IPv4-osoitteita.\n")
                    print("Aloitetaan sulkemalla pois sellaiset IPv4-osoitteet, joita ei haluta jaettavan. Verkossa jotkin laitteet saattavat tarvita staattisia eli pysyviä IP-osoitteita, joten niitä ei haluta jakaa muille laitteille.")
                    print("Anna siis seuraava komento reitittimelle, josta haluat muodostaa DHCPv4-palvelimen: ~ip dhcp excluded-address X.X.X.X Y.Y.Y.Y~. Komennossa suljetaan pois tietty osoiteväli.")
                    print("Esimerkiksi jos haluat sulkea osoitevälin 192.168.10.1 - 192.168.10.9, laitat kyseiset osoitteet X- ja Y-kirjaimien paikalle.\n")

                    print("Kun tietyt osoitteet ovat suljettu pois jaosta, on aika määritellä, mitkä IP-osoitteet vastaavasti myönnetään reitittimen jaettavaksi.")
                    print("Tässä käydään läpi yhdelle aliverkolle myönnettävät IP-osoitteet, joten jos verkossasi on useampi aliverkko, toista seuraavat toimenpiteet niille kaikille.")
                    print("Ensin siis määritellään ns. osoitepoolille nimi. Nimi kannattaa olla kuvainnollinen, esim. LAN-POOL-1.")
                    print("Komento on: ~ip dhcp pool X~. Komennon annettuasi nimetyn mukainen pool muodostetaan, ja reititin siirtyy DHCP-konfigurointitilaan.\n")

                    print("Seuraavaksi konfiguroidaan edellä luotu pool. Pakollisia komentoja ovat verkon osoitteen määrittäminen sekä oletusyhdyskäytävä-reititin.")
                    print("Oletusyhdyskäytävä-reitittimeksi valitaan yleensä host-laitteita lähimpänä olevin reititin tai vaihtoehtoisesti VLAN-verkon yhdyskäytäväosoite. Vähintään yksi täytyy valita.")
                    print("Verkon, jolle DHCPv4-palveluja määrität, osoitteen määrität komennolla ~network X.X.X.X Y.Y.Y.Y~, jossa X-kirjaimet vastaavat verkon IP-osoitetta ja Y-kirjaimet sen maskia.")
                    print("Oletusyhdyskäytävä-reitittimen määrität komennolla ~default-router X.X.X.X~, eli tämä reititin toimii edellä kerrotun verkon oletusyhdyskäytävänä.\n")

                    print("Mikäli jostain syystä haluat ottaa DHCPv4-palvelun reitittimestä pois päältä, anna seuraava komento: ~no service dhcp~.")
                    print("DHCPv4-palvelun saa reitittimeen takaisin päälle komennolla ~service dhcp~.")


                elif koklukusyote == 2:
                    print("\nMikäli oman verkon reititintä ei ole konfiguroitu toimimaan DHCPv4-palvelimena eikä näin ole tarkoitus tehdäkään, sisäverkosta lähtevät osoitepyynnöt voidaan ohjata oman verkon ulkopuoliselle DHCPv4-palvelimelle.")
                    print("Tähän riittää vain kaksi komentoa; ~interface [fastEthernet / gigabitEthernet / serial] X/X~ sekä ~ip helper-address X.X.X.X~.")
                    print("Ensimmäisessä komennossa valitaan reitittimen sisäverkkoa kohti suuntaava liitäntä, ja helper-osoitteeksi määritetään verkon ulkopuolisen DHCP-palvelimen IPv4-osoite.")

                elif koklukusyote == 3:
                   print("\nReititin yleensä konfiguroidaan DHCP-client-laitteeksi, kun internetpalveluntarjoaja (ISP) tarjoaa IP-osoiteinformaatiot. Tätä tehdään useasti pienissä toimistoissa, kotitoimistoissa tai sivukonttoreissa.")
                   print("\nKonfigurointi suoritetaan siten, että määritetään tietty reitittimen Ethernet-liitäntä DHCP-clientiksi.")
                   print("Siirry siis haluamasi liitännän konfigurointiin komennolla ~interface [fastEthernet / gigabitEthernet / serial] X/X~, ja anna liitännälle komento ~ip address dhcp~. Muista myös avata liitäntä komennolla ~no shutdown~.")

                elif koklukusyote == 4:
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-4. Valitse jokin toiminto väliltä 1-4.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-4.")


def Osio11():
    #Osio 11 ajaa vaihtoehdon 10 eli miten konfiguroidaan NAT

    #3D-otsikko
    T = "NAT"
    ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
    print(ASCII_art_1)

    while True:

        print("\nNAT-konfiguraatiovaihtoehtoja on seuraavanlaisesti:\n1 - Staattisen NAT:n konfigurointi\n2 - Dynaamisen NAT:n konfigurointi\n3 - PAT:n konfigurointi\n4 - Haluan palata päävalikkoon")
        syote = input("Valitse toiminto 1-4 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 5):

                if koklukusyote == 1:
                    print("\nStaattinen NAT tarkoittaa, että sisäverkon laitteelle määritetään staattinen julkinen osoite.")
                    print("Pysyvä julkinen osoite on tarpeen esimerkiksi web-palvelimille, jotta ne aina löytyisivät samalla IP-osoitteella.")
                    print("\nStaattinen NAT toteutetaan siten, että luodaan yhteys laitteen inside local- ja inside global-osoitteiden välille.")
                    print("Tämä tapahtuu komennolla ~ip nat inside source static X.X.X.X Y.Y.Y.Y~, jossa X-kirjaimet vastaavat yksityistä osoitetta ja Y-kirjaimet julkista osoitetta.")
                    print("\nLisäksi tarvitsee vielä konfiguroida kaikki reitittimen portit sen mukaan, missä suunnassa sisäverkko ja internet sijaitsevat.")
                    print("Siirry siis liitäntään (~interface [fastEthernet / gigabitEthernet / serial] X/X~), ja anna komento ~ip nat inside~ tai ~ip nat outside~ riippuen, osoittaako liitäntä sisä- vai ulkoverkon suuntaan.\n")
                      
                elif koklukusyote == 2:
                    print("\nDynaaminen NAT tarkoittaa, että yksittäisten yksityisten ja julkisten osoitteiden yhdistämisen sijaan hyödynnetään NAT-poolia, josta NAT-reititin poimii laitteille julkisia IP-osoitteita.")
                    print("Tyypillisesti verkon host-laitteet saavat osoitteensa dynaamisesti, koska niillä ei ole tarvetta aina samalle julkiselle IP-osoitteelle.")
                    print("\nAloitetaan konfigurointi muodostamalla perusmuotoinen pääsyvalvontalista (access control list, ACL).")
                    print("Tämä onnistuu komennolla ~access-list Z permit X.X.X.X Y.Y.Y.Y~. Z:n tilalle asetetaan listan nimi tai numero, tämän saa itse valita.")
                    print("X-kirjainten tilalle se verkko, jonka yksityiset osoitteet NAT saa kääntää julkisiksi. Y-kirjainten tilalle kyseisen verkon villikorttimaski eli esim. /16 verkon villikorttimaski 0.0.255.255.")
                    print("\nSeuraavaksi määritellään osoite-pool, josta julkisia osoitteita myönnetään laitteille.")
                    print("Anna komento ~ip nat pool Z X.X.X.X Y.Y.Y.Y netmask U.U.U.U~, jossa Z on osoite-poolin nimi (keksi itse), X- ja Y-kirjaimet osoiteväli, josta osoitteita poimitaan, ja U-kirjaimet netmask.")
                    print("Netmask määräytyy sen mukaan, montako host-laitetta verkossa on, eli monelleko host-laitteelle täytyy myöntää julkinen IP-osoite. Käytä tarvittaessa aliverkkolaskinta.")
                    print("\nKun ACL ja NAT-pool ovat luotu, jäljelle jää vielä niiden yhdistäminen toisiinsa.")
                    print("Anna siis komento ~ip nat inside source list X pool Y~, jossa X on ACL:n nimi/numero ja Y osoite-poolin nimi.")
                    print("\nLisäksi tarvitsee vielä konfiguroida kaikki reitittimen portit sen mukaan, missä suunnassa sisäverkko ja internet sijaitsevat.")
                    print("Siirry siis liitäntään (~interface [fastEthernet / gigabitEthernet / serial] X/X~), ja anna komento ~ip nat inside~ tai ~ip nat outside~ riippuen, osoittaako liitäntä sisä- vai ulkoverkon suuntaan.\n")

                elif koklukusyote == 3:
                    print("\nPAT (Port Address Translation) voidaan konfiguroida siten, että ISP myöntää vain yhden julkisen osoitteen, tai siten, että ISP myöntää usean julkisen osoitteen.\n")
                    print("Tällä metodilla liikenteen yksilöinti tapahtuu porttinumeroiden perusteella.")

                    while True:

                        print("\nHaluatko konfiguroida PAT:n siten, että\n1 - ISP myöntää vain yhden julkisen osoitteen\n2 - ISP myöntää usean julkisen osoitteen\n3 - Haluan palata edelliseen valikkoon")
                        alisyote = input("Valitse toiminto 1-3 (kirjoita numero): ")

                        #Käyttäjän syötteen tarkistus
                        try:

                            alikoklukusyote = int(alisyote)
                            if (alikoklukusyote > 0 and alikoklukusyote < 4):

                                if alikoklukusyote == 1:
                                    print("\nHaluat siis konfiguroida PAT:n siten, että ISP myöntää vain yhden julkisen IP-osoitteen.")
                                    print("\nAloitetaan konfiguroimalla perusmuotoinen ACL, jotta sallitaan vain ne IP-osoitteet, jotka tarvitsee kääntää julkiseksi.")
                                    print("Anna komento ~access-list Z permit X.X.X.X Y.Y.Y.Y~. Z:n tilalle asetetaan listan nimi tai numero, tämän saa itse valita.")
                                    print("X-kirjainten tilalle se verkko, jonka yksityiset osoitteet NAT saa kääntää julkisiksi. Y-kirjainten tilalle kyseisen verkon villikorttimaski eli esim. /16 verkon villikorttimaski 0.0.255.255.")
                                    print("\nSeuraavaksi annetaan komento, jonka ansiosta kaikki internetiin kulkevan liikenteen lähteen IP-osoitteeksi tulee NAT-reitittimen internetin suuntaan olevan liitännän IP-osoite.")
                                    print("Lisäksi liikenne yksilöidään porttinumeroiden perusteella avainsanan 'overload' ansiosta.")
                                    print("Komento on: ~ip nat inside source list X interface [fastEthernet / gigabitEthernet / serial] X/X overload~. X:n tilalle kirjoita ACL:n nimi/numero.")
                                    print("\nLisäksi tarvitsee vielä konfiguroida kaikki reitittimen portit sen mukaan, missä suunnassa sisäverkko ja internet sijaitsevat.")
                                    print("Siirry siis liitäntään (~interface [fastEthernet / gigabitEthernet / serial] X/X~), ja anna komento ~ip nat inside~ tai ~ip nat outside~ riippuen, osoittaako liitäntä sisä- vai ulkoverkon suuntaan.\n")

                                elif alikoklukusyote == 2:
                                    print("\nHaluat siis konfiguroida PAT:n siten, että ISP myöntää useita julkisia IP-osoitteita.")
                                    print("\nAloitetaan konfigurointi muodostamalla perusmuotoinen pääsyvalvontalista (access control list, ACL).")
                                    print("Tämä onnistuu komennolla ~access-list Z permit X.X.X.X Y.Y.Y.Y~. Z:n tilalle asetetaan listan nimi tai numero, tämän saa itse valita.")
                                    print("X-kirjainten tilalle se verkko, jonka yksityiset osoitteet NAT saa kääntää julkisiksi. Y-kirjainten tilalle kyseisen verkon villikorttimaski eli esim. /16 verkon villikorttimaski 0.0.255.255.")
                                    print("\nSeuraavaksi määritellään osoite-pool, josta julkisia osoitteita myönnetään laitteille.")
                                    print("Anna komento ~ip nat pool Z X.X.X.X Y.Y.Y.Y netmask U.U.U.U~, jossa Z on osoite-poolin nimi (keksi itse), X- ja Y-kirjaimet osoiteväli, josta osoitteita poimitaan, ja U-kirjaimet netmask.")
                                    print("Netmask määräytyy sen mukaan, montako host-laitetta verkossa on, eli monelleko host-laitteelle täytyy myöntää julkinen IP-osoite. Käytä tarvittaessa aliverkkolaskinta.")
                                    print("\nYhdistetään ACL ja osoite-pool komennolla ~ip nat inside source list X pool Y overload~. Kirjoita X:n tilalle ACL:n nimi/numero, ja Y:n tilalle NAT-poolin nimi.")
                                    print("\nLisäksi tarvitsee vielä konfiguroida kaikki reitittimen portit sen mukaan, missä suunnassa sisäverkko ja internet sijaitsevat.")
                                    print("Siirry siis liitäntään (~interface [fastEthernet / gigabitEthernet / serial] X/X~), ja anna komento ~ip nat inside~ tai ~ip nat outside~ riippuen, osoittaako liitäntä sisä- vai ulkoverkon suuntaan.\n")

                                elif alikoklukusyote == 3:
                                    break

                            else:
                                print("Syöttämäsi valinta ei ollut väliltä 1-3. Valitse jokin toiminto väliltä 1-3.")

                        except:
                            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-3.")

                elif koklukusyote == 4:
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-4. Valitse jokin toiminto väliltä 1-4.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-4.")


def Osio12():
    #Osio 12 ajaa vaihtoehdon 11 eli miten asetetaan kytkimelle/reitittimelle ensimmäiset turvallisuusmääritykset
    print("Alla on esitelty tärkeimpiä ensimmäisiä turvallisuusmäärityksiä, joita reitittimelle ja kytkimelle kannattaa asettaa.")
    print("\nVAHVAN KRYPTATUN SALASANAN ASETTAMINEN ENABLE-TILAAN. (anna väh. 10-merkkinen salasana)\nAnna 'config'-tilassa komento ~enable secret X~.")
    print("\nLAITTEEN SALASANOJEN KRYPTAUS.\nAnna 'config'-tilassa komento ~service password-encryption~.")
    print("\nBANNERIN ASETTAMINEN.\nAnna 'config'-tilassa komento ~banner motd #X#~.")
    print("\nASETA SALASANALLE MERKKIPITUUSVAATIMUS (vain reitittimelle).\nAnna 'config'-tilassa komento ~security password min-length X~.")
    print("\nESTÄ KIRJAUTUMINEN X MINUUTIKSI, MIKÄLI KÄYTTÄJÄ EPÄONNISTUU KIRJAUTUMISESSA Y KERTAA Z SEKUNNIN aikana (vain reitittimelle).\nAnna 'config'-tilassa komento ~login block-for X attempts Y within Z~.")
    print("\nASETA KONSOLISALASANA JA MÄÄRITÄ ISTUNTO KATKEAMAAN Y MINUUTIN KULUTTUA, JOS TOIMINTA ON EPÄAKTIIVISTA.\nAnna 'config'-tilassa komento ~line console 0~, jonka jälkeen 'config-line'-tilassa komennot ~password X~ ja ~login~.")
    print("Jatka vielä 'config-line'-tilassa komennolla ~exec-timeout Y~, jolla määrität montako minuuttia istunto pysyy ylhäällä ennen katkeamista, mikäli käyttäjä ei ole aktiivinen.")
    print("Saman voit tehdä myös vty-linjoille, jolloin annat komennon ~line console 0~ sijaan reitittimellä komennon ~line vty 0 4~ ja kytkimellä ~line vty 0 15~, ja annat loput komennot yllä kuvaillulla tavalla.")


def Osio13():
    #Osio 13 ajaa vaihtoehdon 12 eli miten kytkimeen/reitittimeen konfiguroidaan SSH-yhteys

    #3D-otsikko
    T = "SSH"
    ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
    print(ASCII_art_1)

    print("Ensimmäiseksi tarkasta, tukeeko laitteesi SSH-protokollaa. Anna laitteellasi komento ~show ip ssh~, ja mikäli komento tunnistetaan, laite tukee SSH:ta.\nSeuraavilla ohjeilla konfiguroit SSH-yhteyden:")
    print("\nANNA VERKON DOMAIN-NIMI.\nAnna 'config'-tilassa komento ~ip domain-name X~.")
    print("\nKYTKE DNS-LOOKUP POIS PÄÄLTÄ (jotta reititin ei yritä kääntää väärin annettuja komentoja).\nAnna 'config'-tilassa komento ~no ip domain-lookup~.")
    print("\nMUODOSTA RSA-AVAINPARI (suositeltavaa luoda väh. 1024-bittinen avainpari).\nAnna 'config'-tilassa komento ~crypto key generate rsa~ ja kirjoita, minkäbittisen avainparin haluat (512, 1024, 2048...).")
    print("\nMUODOSTA PÄÄSY PAIKALLISEEN TIETOKANTAAN (paikallinen autentikointi).\nAnna 'config'-tilassa komento ~username X secret Y~, jossa X on käyttäjätunnus ja Y kryptattu salasana.")
    print("\nOTA TURVALLISEMPI SSH-VERSIO KÄYTTÖÖN.\nAnna 'config'-tilassa komento ~ip ssh version 2~.")
    print("\nKONFIGUROI VTY-LINJAT.\nAnna 'config'-tilassa reitittimelle komento ~line vty 0 4~ ja kytkimelle komento ~line vty 0 15~, jonka jälkeen 'config-line'-tilassa komennot ~login local~ ja ~transport input ssh~.")


def Osio14():
    #Osio 14 ajaa vaihtoehdon 13 eli miten kytkimeen konfiguroidaan erilaisia turvallisuusmäärityksiä
    print("Tässä osiossa käsitellään kytkimen turvallisuuskonfigurointeja. Osio on jaettu porttiturvallisuuteen, sekä VLAN-, DHCP-, ARP- ja STP-hyökkäyksiltä suojautumiseen.")

    while True:

        print("\nMitä haluat tehdä?\n1 - Konfiguroida porttien turvallisuutta\n2 - Suojautua VLAN-hyökkäyksiltä\n3 - Suojautua DHCP-hyökkäyksiltä\n4 - Suojautua ARP-hyökkäyksiltä\n5 - Suojautua STP-hyökkäyksiltä\n6 - Palata päävalikkoon")
        syote = input("Valitse toiminto 1-6 (kirjoita numero): ")

        #Käyttäjän syötteen tarkistus
        try:

            koklukusyote = int(syote)
            if (koklukusyote > 0 and koklukusyote < 7):

                if koklukusyote == 1:
                    print("\nValitse ensin portti, jota aletaan konfiguroimaan. Anna komento ~interface [fastEthernet / gigabitEthernet] X/X~.")
                    print("Salli portin access-tila ja turvallisuus komennoilla ~switchport mode access~ ja ~switchport port-security~.")
                    print("\nSeuraavaksi voit määritellä edellä valittuun porttiin joitain tärkeitä seuraavia turvallisuusominaisuuksia.")
                    print("Asetetaan porttiin liitettävien MAC-osoitteiden maksimimääräksi X komennolla ~switchport port-security maximum X~. Kun määrä tulee täyteen, portti ei enää hyväksy uusia MAC-osoitteita.")
                    print("Kerrotaan portille turvalliseksi tiedetty MAC-osoite AAAA.BBBB.1234 komennolla ~switchport port-security mac-address AAAA.BBBB.1234~. Tämän jälkeen porttiin ei voi liittää muita MAC-osoitteita.")
                    print("Aseta portti unohtamaan siihen liitetyt MAC-osoitteet X minuutin kuluessa komennolla ~switchport port-security aging time X~.")
                    print("Määritä mitä kytkin tekee, kun porttiin liitetty MAC-osoite ei kuulu turvalliseksi luokiteltuihin osoitteisiin. Komento on ~switchport port-security violation shutdown / restrict / protect~.")
                    print("Shutdown = portti menee välittömästi pois käytöstä, restrict = tuntemattomien MAC-osoitteiden paketit pudotetaan ja tapahtuneesta ilmoitetaan, protect = tuntemattomien MAC-osoitteiden paketit vain pudotetaan.")
                    print("\nKytkimestä kannattaa sulkea kaikki käyttämättömät portit, komennoilla ~interface range [fastEthernet / gigabitEthernet] X/X-Y~ ja ~shutdown~.")
    
                elif koklukusyote == 2:
                    print("\nEstä DTP-ehdotukset eli automaattinen trunk-määritys porteissa, jotka eivät ole trunk-portteja.")
                    print("Siirry kyseisiin portteihin komennolla ~interface range [fastEthernet / gigabitEthernet] X/X-Y~ ja anna komento ~switchport mode access~, jolloin portit siirtyvät access-tilaan.")
                    print("\nOta käyttämättömät portit pois käytöstä ja aseta ne käyttämättömään VLAN:iin.")
                    print("Siirry kyseisiin portteihin komennolla ~interface range [fastEthernet / gigabitEthernet] X/X-Y~, aseta ne access-tilaan komennolla ~switchport mode access~, ja siirrä portit käyttämättömään VLAN:iin komennolla ~switchport access vlan X~.")
                    print("Muista myös sulkea nämä portit komennolla ~shutdown~.")
                    print("\nSallitaan trunk-yhteys trunk-porteissa, ja kielletään DTP-ehdotukset näissä. Lisäksi asetetaan native-VLAN joksikin muuksi kuin VLAN 1:ksi.")
                    print("Siirry siis ensin trunk-portteihin ~interface range [fastEthernet / gigabitEthernet] X/X-Y~, aseta ne trunk-tilaan komennolla ~switchport mode trunk~, ja kielletään DTP-ehdotukset ~switchport nonegotiate~.")
                    print("Native-VLAN asetetaan komennolla ~switchport trunk native vlan X~, jossa X on jokin muu kuin 1.")

                elif koklukusyote == 3:
                    print("\nDHCP-snooping on tekniikka, joka pyrkii estämään oikeudettomien DHCP-palvelinten pääsyn sisäverkkoon.")
                    print("\nSallitaan DHCP-snooping 'config'-tilassa komennolla ~ip dhcp snooping~. Tämä voidaan sallia myös halutuissa VLAN:eissa 'config'-tilassa komennolla ~ip dhcp snooping vlan X,Y,Z~.")
                    print("\nLuotettaville porteille kannattaa antaa komento ~ip dhcp snooping trust~. Anna tämä komento siis komennon ~interface range [fastEthernet / gigabitEthernet] X/X-Y~ jälkeen.")
                    print("\nRajoita DHCPDISCOVERY-viestien, joita on mahdollista vastaanottaa per sekunti, määrää. Tämä toiminto tehdään epäluotettaville porteille.")
                    print("\nAnna jälleen ~interface range [fastEthernet / gigabitEthernet] X/X-Y~, jonka jälkeen ~ip dhcp snooping limit rate X~.")

                elif koklukusyote == 4:
                    print("\nMyös ARP-hyökkäyksiin liittyy DHCP-hyökkäykset, joten salli DHCP-snooping (kts. kohta 3, DHCP-hyökkäyksiltä suojautuminen).")
                    print("\nSallitaan DAI (Dynamic ARP Inspection) samoissa VLAN:eissa, joihin on myös DHCP-snooping määritelty. Anna siis komento ~ip arp inspection vlan X~.")
                    print("\nSiirry luotettaviksi luokiteltaviin portteihin komennolla ~interface range [fastEthernet / gigabitEthernet] X/X-Y~ ja anna komennot ~ip dhcp snooping trust~ sekä ~ip arp inspection trust~.")

                elif koklukusyote == 5:
                    print("\nSTP-hyökkäyksiä (Spanning Tree Protocol) vastaan on kehitetty BPDU-guard-niminen tekniikka.")
                    print("\nTämä voidaan konfiguroida kaikille PortFast-sallituille porteille komennolla ~spanning-tree portfast bpduguard default~.")
                    print("Vastaavasti BPDU-guard voidaan konfiguroida myös yksittäisiin portteihin. Siirry haluamaasi porttiin komennolla ~interface [fastEthernet / gigabitEthernet] X/X~, ja anna komento ~spanning-tree bpduguard enable~.")

                elif koklukusyote == 6:
                    break

            else:
                print("Syöttämäsi valinta ei ollut väliltä 1-6. Valitse jokin toiminto väliltä 1-6.")

        except:
            print("Syötit virheellisen arvon. Valitse jokin toiminto väliltä 1-6.")


#Ajetaan koodi
Osio1()