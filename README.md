# Ciscon reitittimien ja kytkimien konfiguroinnin cheatsheet

Tämä ohjelma sisältää rautalankamalleja Ciscon reitittimien ja kytkimien erilaisiin komentorivipohjaisiin konfigurointeihin. 

## Ohjelman kuvaus

Ohjelma on jaettu konfigurointien mukaan 13 eri osioon:

1. Vanhojen konfiguraatioiden poistaminen
2. Ensimmäiset toimenpiteet konfiguroimattomalle kytkimelle/reitittimelle
3. Reitittimen liitäntöjen konfigurointi (IPv4)
4. Hallinta- ja oletusyhdyskäytäväosoitteen (IPv4) asettaminen kytkimelle
5. VLAN-verkkojen konfigurointi
6. EtherChannelin konfigurointi kytkinten välille
7. Staattisten, oletus- ja host-reittien konfigurointi reitittimelle
8. OSPFv2:n konfigurointi reitittimelle
9. DHCPv4:n konfigurointi reitittimelle
10. NAT:n konfigurointi reitittimelle
11. Ensimmäisten turvallisuusmääritysten konfigurointi kytkimelle/reitittimelle
12. SSH-yhteyden konfigurointi kytkimelle/reitittimelle
13. Muiden turvallisuusmääritysten konfigurointi kytkimelle

## Ohjelman käyttöönottaminen

Ohjelma on toteutettu Python-ohjelmointikielellä, joten sen suorittamiseen vaaditaan Python-ohjelman asennus. Voit ottaa ohjelman käyttöön esimerkiksi seuraavia ohjeita noudattaen:

1. Lataa Python. Voit ladata käyttöjärjestelmällesi sopivan version osoitteesta https://www.python.org/downloads/ tai laitteesi sovelluskaupasta.
2. Kopioi ohjelman koodi itsellesi valitsemalla GitHub-repositoriostani ohjelma 'CiscoCheatSheet_OH.py' --> Klikkaa painiketta 'Raw' --> Maalaa koodi esimerkiksi painamalla CTRL + A --> Kopioi koodi --> Liitä koodi esimerkiksi muistioon/notepadiin --> Tallenna tiedosto laitteellesi .py-tiedostona eli esimerkiksi 'tiedostonimi.py'.
3. Hae resurssienhallinnasta tallentamasi .py-tiedosto --> Klikkaa tiedostoa hiiren oikealla painikkeella --> 'Kopioi polkuna'.
4. Siirry laitteesi komentokehotteeseen, esimerkiksi kirjoittamalla hakuun 'cmd' --> Kirjoita komentokehotteeseen 'pip install pyfiglet', joka asentaa ohjelmassa käytettävän lisämoduulin --> Kun lisämoduuli on asennettu, kirjoita komentokehotteeseen 'python ', liitä sen perään kopioimasi tiedostopolku ja paina Enter.
5. Ohjelma on valmis käytettäväksi.

## Huomioita

Ohjelmassa liikutaan eri osioiden välillä kirjoittamalla haluamaansa vaihtoehtoa vastaava numero komentokehotteeseen.

Ohjelmassa esitetyt konfigurointitavat ovat vain yksinkertaisia esimerkkejä, eivätkä ne välttämättä ole ainoita oikeita tapoja konfiguroida. Soveltavammissa tilanteissa komentoihin löydät apua laitteiden komentorivillä kysymysmerkin (?) avulla.

Komennot ovat esitetty aaltoviivojen sisällä.

## Tekijä

@oskariheinonen
