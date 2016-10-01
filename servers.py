def get_servers():
    servers ={ "server1": [
                ["Eastlink Atlantic (AS 11260)", "Eastlink Atlantic (AS 11260)" ],
                ["Eastlink Eastern (AS 23184)", "Eastlink Eastern (AS 23184)" ] ,
                ["Eastlink Pacific (AS 22799)","Eastlink Pacific (AS 22799)" ],
                ["Allstream (AS 15290)", "Eastlink Pacific (AS 22799)"],
                ["AT&amp;T (AS 7018)", "AT&amp;T (AS 7018)"],
                ["Belwue (AS 553)", "Belwue (AS 553)" ],
                ["Comcast (AS 7922)", "Comcast (AS 7922)"],
                ["Eunet (AS 6667)", "Eunet (AS 6667)"],
                ["Exodus Communications (AS 3967)", "Exodus Communications (AS 3967)" ],
                ["Global Crossing (AS 3549)", "Global Crossing (AS 3549)"],
                ["Global Crossing Europe (AS 3549)", "Global Crossing Europe (AS 3549)"],
                ["Group Telecom - east (AS 6539)", "Group Telecom - east (AS 6539)"],
                ["Host.net (AS 13645)", "Host.net (AS 13645)"],
                ["Hurricane Electric (AS 6939)","Hurricane Electric (AS 6939)" ],
                ["nLayer (AS 4436)", "nLayer (AS 4436)" ],
                ["Nodus Network", "Nodus Network" ],
                ["Opentransit (AS 5511)", "Opentransit (AS 5511)"],
                ["Optus (AS 7474)", "Optus (AS 7474)"],
                ["Oregon Exchange (AS 6447)", "Oregon Exchange (AS 6447)"],
                ["Rogers (AS 812)", "Rogers (AS 812)"],
                ["SAIX (AS 5713)", "SAIX (AS 5713)"],
                ["Savvis (AS 3561)", "Savvis (AS 3561)"],
                ["Sunrise (AS 6730)", "Sunrise (AS 6730)"],
                ["Swisscom IP+ (AS 3303)", "Swisscom IP+ (AS 3303)"],
                ["Switch (AS 23005)", "Switch (AS 23005)"],
                ["TDC (AS 3292)", "TDC (AS 3292)"],
                ["Time Warner (AS 4323)", "Time Warner (AS 4323)"],
                ["TiNET (AS 3257)", "TiNET (AS 3257)" ],
                ["TELUS East (AS 852)",  "TELUS East (AS 852)"],
                ["University of Washin,gton (AS 6447)", "University of Washin,gton (AS 6447)"],
                ["Videotron (AS 5769)", "Videotron (AS 5769)"],
                ["r20-Tln-TIX", "r20-Tln-TIX"],
                ["ML Online (AS 5546)", "ML Online (AS 5546)"],
                ["kj-gw", "kj-gw" ],
                ["rtr1","rtr1" ],
                ["INXS", "INXS"],
                ["LINX (UK)", "LINX (UK)"],
                ["LINX (Transit)", "LINX (Transit)"],
                ["LINX (Multicast)", "LINX (Multicast)"],
                ["zebra", "zebra" ],
                ["Amsterdam (NL), AMS-IX", "Amsterdam (NL), AMS-IX"],
                ["Amsterdam (NL), AMS-IX",  "Amsterdam (NL), AMS-IX"],
                ["Copenhagen/Lyngby (DK), DIX #1", "Copenhagen/Lyngby (DK), DIX #1"],
                ["Copenhagen/Virum (DK), DIX #2", "Copenhagen/Virum (DK), DIX #2"],
                ["Frankfurt (DE), DE-CIX",  "Frankfurt (DE), DE-CIX"],
                ["London (UK), LINX #1", "London (UK), LINX #1" ],
                ["London (UK), LINX #2","London (UK), LINX #2" ],
                ["New York 1 (US)", "New York 1 (US)" ],
                ["New York 2 (US)", "New York 2 (US)" ],
                ["New York 3 (US)", "New York 3 (US)"],
                ["Oslo (NO), NIX1", "Oslo (NO), NIX1" ],
                ["Oslo (NO), NIX2","Oslo (NO), NIX2" ],
                ["Stockholm (SE), Netnod", "Stockholm (SE), Netnod"],
                ["Amsterdam", "Amsterdam"],
                ["Antwerp", "Antwerp"],
                ["Berlin", "Berlin"],
                ["Brussels", "Brussels"],
                ["Dublin", "Dublin"],
                ["Frankfurt", "Frankfurt"],
                ["Leiden", "Leiden"],
                ["London", "London"],
                ["Munich", "Munich"],
                ["Rotterdam", "Rotterdam" ],
                ["D-GIX (DPT)", "D-GIX (DPT)"],
                ["D-GIX (FDDI)", "D-GIX (FDDI)" ],
                ["Level3 (AS 3356)", "Level3 (AS 3356)"],
                ["Davidov Electric (AS 12814)", "Davidov Electric (AS 12814)"],
                ["Tata Communications (AS6453)", "Tata Communications (AS6453)"],
                ["Bell Canada (AS577)", "Bell Canada (AS577)"],
                ["Data Telecom IPv6", "Data Telecom IPv6" ],
                ["6TAP", "6TAP" ],
                ["LavaNet", "LavaNet"],
                ["r1-gw.ipv6.itk.pl", "r1-gw.ipv6.itk.pl"],
                ["EdisonTel IPv6", "EdisonTel IPv6"],
            ], 
            "server2": [
                ["Asia" ,"Asia"],
                ["119637","Chai Wan, CHINA - CLK1"],
                ["145522","Chuo-ku, Tokyo, JAPAN - TYO1"],
                ["145366","Singapore, SINGAPORE - QPG1"],
                ["Europe" ,"Europe"],
                ["146702","Ultimo, AUSTRALIA - RSE1"],
                ["149996"," Hamburg, GERMANY - HAM1"],
                ["119611","Amsterdam, NETHERLANDS - AMS2"],
                ["118042","Antwerp, BELGIUM - NDL1.ANT"],
                ["149904","Basingstoke, Hampshire, UNITED KINGDOM - BBS1"],
                ["150196","Berlin, GERMANY - KIT1.BER"],
                ["147205","Dublin, IRELAND - DUB1"],
                ["137782","Frankfurt, GERMANY - FRA4"],
                ["149982","Glostrup, DENMARK - CPH1"],
                ["154931","Helsinki, FINLAND - HEL1"],
                ["149302","Leeds, UNITED KINGDOM - LBA1"],
                ["149262","Leigh, UNITED KINGDOM - MAN1"],
                ["152202","London, UNITED KINGDOM - LON2"],
                ["131962","London, UNITED KINGDOM - LON3"],
                ["154771","Luxembourg, LUXEMBOURG - BCE1.LUX"],
                ["137731","Madrid, SPAIN - MAD1"],
                ["186781","Milano, ITALY - LIN1"],
                ["149362","Munich, GERMANY - MUN1"],
                ["149276","Nottingham, UNITED KINGDOM - NQT1"],
                ["104830","Oslo, NORWAY - OSL2"],
                ["152142","Paris, FRANCE - CDG3"],
                ["154731","Rotterdam, NETHERLANDS - VDG1.RTM"],
                ["154360","Slough, UNITED KINGDOM - LHR1"],
                ["153980","Solihull, UNITED KINGDOM - BHX1"],
                ["145146","Stockholm, SWEDEN - ARN3"],
                ["150227","Stuttgart, GERMANY - VDL1.STR"],
                ["Latin America" , "Latin America"],
                ["154487","Vienna, AUSTRIA - VIE1"],
                ["407018","Bogota, COLUMBIA - CXV1.BOG"],
                ["153102","Buenos Aires, ARGENTINA - EZE1"],
                ["153584","Panama City, PANAMA - PTY1"],
                ["407165","Quito, ECUADOR - TUI1.UIO"],
                ["153622","Santiago, CHILE - SCL1"],
                ["154024","Sao Cristavao, Rio de Janeiro, BRAZIL - GIG1"],
                ["US" , "US"],
                ["153562","Sao Paulo, BRAZIL - GRU1"],
                ["144523","Anaheim, UNITED STATES - SNA1"],
                ["153887","Ashburn, UNITED STATES - DCA3"],
                ["119621","Atlanta, UNITED STATES - ATL1"],
                ["154394","Baltimore, UNITED STATES - BWI1.BWI"],
                ["145705","Boston, UNITED STATES - BOS1"],
                ["118462","Chicago, UNITED STATES - CHI1"],
                ["137902","Cleveland, UNITED STATES - CLE1"],
                ["118468","Dallas, UNITED STATES - DAL1"],
                ["137719","Denver, UNITED STATES - DEN2"],
                ["146667","Houston, UNITED STATES - HOU1"],
                ["137725","Indianapolis, UNITED STATES - IND1"],
                ["145422","Kansas City, UNITED STATES - KCY1"],
                ["118724","Los Angeles, UNITED STATES - LAX1"],
                ["131943","Miami, UNITED STATES - MIA1"],
                ["104714","Miami, UNITED STATES - MIA2"],
                ["151255","Milwaukee, UNITED STATES - MKE1.MKE"],
                ["144422","Minneapolis, UNITED STATES - MIN1"],
                ["119403","New York, UNITED STATES - JFK1"],
                ["154059","Palo Alto, UNITED STATES - PAO2"],
                ["119643","Philadelphia, UNITED STATES - PHI1"],
                ["119409","Phoenix, UNITED STATES - PHX1"],
                ["163364","Pittsburgh, UNITED STATES - PIT2.PIT"],
                ["150042","Rochester, UNITED STATES - ROC1"],
                ["137803","Sacramento, UNITED STATES - SAC1"],
                ["149962","Saint Louis, UNITED STATES - STL1.STL"],
                ["149316","San Diego, UNITED STATES - SAN1"],
                ["154077","San Jose, UNITED STATES - SJC2"],
                ["192297","Seattle, UNITED STATES - SEA1"],
                ["147487","Southfield, UNITED STATES - DET1"],
                ["119649","Sunnyvale, UNITED STATES - SNV2"],
                ["146167","Tampa, UNITED STATES - TPA1"],
                ["144482","Toronto, CANADA - YYZ1"],
                ["135272","Washington, UNITED STATES - WDC2"],
                    ],
            }

    return servers


if __name__ == "__main__":
    servers = get_servers()
    
    global_crossing = servers["server1"]
    east = servers["server2"]

    for server in servers["server1"]:
        print (server)
