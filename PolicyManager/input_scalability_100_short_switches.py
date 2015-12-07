############################ INPUT ############################
"""
runs with "1221.r0.reachable.graph"
calculates paths from "Broadcast" through 1 MB to "zones" and through 2 MBs to "admins"
additionally calculates dags to all admins

170 zones and admins:
took 7 secs for policy manager
took 9 secs for paths solver on graph 1755                (without writing to files!!)
took 19 secs for paths solver on graph 1221 (reachable)    (without writing to files!!)
took 60 secs for paths solver on graph 1239                (without writing to files!!)

311 zones and admins:
took 25 secs for policy manager
took 35 secs for paths solver on graph 1221 (reachable)      (without writing to files!!)
took 107 secs for paths solver on graph 1239                  (without writing to files!!)

512 zones and admins:
took 62 secs for policy manager
took 183 secs for paths solver on graph 1239

"""

BROADCAST_IP = "1.1.1.0/24"
BROADCAST2_IP = "1.1.2.0/24"


ZONE_0 = "192.168.0.0/24"
ZONE_1 = "192.168.1.0/24"
ZONE_2 = "192.168.2.0/24"
ZONE_3 = "192.168.3.0/24"
ZONE_4 = "192.168.4.0/24"
ZONE_5 = "192.168.5.0/24"
ZONE_6 = "192.168.6.0/24"
ZONE_7 = "192.168.7.0/24"
ZONE_8 = "192.168.8.0/24"
ZONE_9 = "192.168.9.0/24"
ZONE_10 = "192.168.10.0/24"
ZONE_11 = "192.168.11.0/24"
ZONE_12 = "192.168.12.0/24"
ZONE_13 = "192.168.13.0/24"
ZONE_14 = "192.168.14.0/24"
ZONE_15 = "192.168.15.0/24"
ZONE_16 = "192.168.16.0/24"
ZONE_17 = "192.168.17.0/24"
ZONE_18 = "192.168.18.0/24"
ZONE_19 = "192.168.19.0/24"
ZONE_20 = "192.168.20.0/24"
ZONE_21 = "192.168.21.0/24"
ZONE_22 = "192.168.22.0/24"
ZONE_23 = "192.168.23.0/24"
ZONE_24 = "192.168.24.0/24"
ZONE_25 = "192.168.25.0/24"
ZONE_26 = "192.168.26.0/24"
ZONE_27 = "192.168.27.0/24"
ZONE_28 = "192.168.28.0/24"
ZONE_29 = "192.168.29.0/24"
ZONE_30 = "192.168.30.0/24"
ZONE_31 = "192.168.31.0/24"
ZONE_32 = "192.168.32.0/24"
ZONE_33 = "192.168.33.0/24"
ZONE_34 = "192.168.34.0/24"
ZONE_35 = "192.168.35.0/24"
ZONE_36 = "192.168.36.0/24"
ZONE_37 = "192.168.37.0/24"
ZONE_38 = "192.168.38.0/24"
ZONE_39 = "192.168.39.0/24"
ZONE_40 = "192.168.40.0/24"
ZONE_41 = "192.168.41.0/24"
ZONE_42 = "192.168.42.0/24"
ZONE_43 = "192.168.43.0/24"
ZONE_44 = "192.168.44.0/24"
ZONE_45 = "192.168.45.0/24"
ZONE_46 = "192.168.46.0/24"
ZONE_47 = "192.168.47.0/24"
ZONE_48 = "192.168.48.0/24"
ZONE_49 = "192.168.49.0/24"
ZONE_50 = "192.168.50.0/24"
ZONE_51 = "192.168.51.0/24"
ZONE_52 = "192.168.52.0/24"
ZONE_53 = "192.168.53.0/24"
ZONE_54 = "192.168.54.0/24"
ZONE_55 = "192.168.55.0/24"
ZONE_56 = "192.168.56.0/24"
ZONE_57 = "192.168.57.0/24"
ZONE_58 = "192.168.58.0/24"
ZONE_59 = "192.168.59.0/24"
ZONE_60 = "192.168.60.0/24"
ZONE_61 = "192.168.61.0/24"
ZONE_62 = "192.168.62.0/24"
ZONE_63 = "192.168.63.0/24"
ZONE_64 = "192.168.64.0/24"
ZONE_65 = "192.168.65.0/24"
ZONE_66 = "192.168.66.0/24"
ZONE_67 = "192.168.67.0/24"
ZONE_68 = "192.168.68.0/24"
ZONE_69 = "192.168.69.0/24"
ZONE_70 = "192.168.70.0/24"
ZONE_71 = "192.168.71.0/24"
ZONE_72 = "192.168.72.0/24"
ZONE_73 = "192.168.73.0/24"
ZONE_74 = "192.168.74.0/24"
ZONE_75 = "192.168.75.0/24"
ZONE_76 = "192.168.76.0/24"
ZONE_77 = "192.168.77.0/24"
ZONE_78 = "192.168.78.0/24"
ZONE_79 = "192.168.79.0/24"
ZONE_80 = "192.168.80.0/24"
ZONE_81 = "192.168.81.0/24"
ZONE_82 = "192.168.82.0/24"
ZONE_83 = "192.168.83.0/24"
ZONE_84 = "192.168.84.0/24"
ZONE_85 = "192.168.85.0/24"
ZONE_86 = "192.168.86.0/24"
ZONE_87 = "192.168.87.0/24"
ZONE_88 = "192.168.88.0/24"
ZONE_89 = "192.168.89.0/24"
ZONE_90 = "192.168.90.0/24"
ZONE_91 = "192.168.91.0/24"
ZONE_92 = "192.168.92.0/24"
ZONE_93 = "192.168.93.0/24"
ZONE_94 = "192.168.94.0/24"
ZONE_95 = "192.168.95.0/24"
ZONE_96 = "192.168.96.0/24"
ZONE_97 = "192.168.97.0/24"
ZONE_98 = "192.168.98.0/24"
ZONE_99 = "192.168.99.0/24"


ADMIN_0 = "192.168.0.100/32"
ADMIN_1 = "192.168.1.100/32"
ADMIN_2 = "192.168.2.100/32"
ADMIN_3 = "192.168.3.100/32"
ADMIN_4 = "192.168.4.100/32"
ADMIN_5 = "192.168.5.100/32"
ADMIN_6 = "192.168.6.100/32"
ADMIN_7 = "192.168.7.100/32"
ADMIN_8 = "192.168.8.100/32"
ADMIN_9 = "192.168.9.100/32"
ADMIN_10 = "192.168.10.100/32"
ADMIN_11 = "192.168.11.100/32"
ADMIN_12 = "192.168.12.100/32"
ADMIN_13 = "192.168.13.100/32"
ADMIN_14 = "192.168.14.100/32"
ADMIN_15 = "192.168.15.100/32"
ADMIN_16 = "192.168.16.100/32"
ADMIN_17 = "192.168.17.100/32"
ADMIN_18 = "192.168.18.100/32"
ADMIN_19 = "192.168.19.100/32"
ADMIN_20 = "192.168.20.100/32"
ADMIN_21 = "192.168.21.100/32"
ADMIN_22 = "192.168.22.100/32"
ADMIN_23 = "192.168.23.100/32"
ADMIN_24 = "192.168.24.100/32"
ADMIN_25 = "192.168.25.100/32"
ADMIN_26 = "192.168.26.100/32"
ADMIN_27 = "192.168.27.100/32"
ADMIN_28 = "192.168.28.100/32"
ADMIN_29 = "192.168.29.100/32"
ADMIN_30 = "192.168.30.100/32"
ADMIN_31 = "192.168.31.100/32"
ADMIN_32 = "192.168.32.100/32"
ADMIN_33 = "192.168.33.100/32"
ADMIN_34 = "192.168.34.100/32"
ADMIN_35 = "192.168.35.100/32"
ADMIN_36 = "192.168.36.100/32"
ADMIN_37 = "192.168.37.100/32"
ADMIN_38 = "192.168.38.100/32"
ADMIN_39 = "192.168.39.100/32"
ADMIN_40 = "192.168.40.100/32"
ADMIN_41 = "192.168.41.100/32"
ADMIN_42 = "192.168.42.100/32"
ADMIN_43 = "192.168.43.100/32"
ADMIN_44 = "192.168.44.100/32"
ADMIN_45 = "192.168.45.100/32"
ADMIN_46 = "192.168.46.100/32"
ADMIN_47 = "192.168.47.100/32"
ADMIN_48 = "192.168.48.100/32"
ADMIN_49 = "192.168.49.100/32"
ADMIN_50 = "192.168.50.100/32"
ADMIN_51 = "192.168.51.100/32"
ADMIN_52 = "192.168.52.100/32"
ADMIN_53 = "192.168.53.100/32"
ADMIN_54 = "192.168.54.100/32"
ADMIN_55 = "192.168.55.100/32"
ADMIN_56 = "192.168.56.100/32"
ADMIN_57 = "192.168.57.100/32"
ADMIN_58 = "192.168.58.100/32"
ADMIN_59 = "192.168.59.100/32"
ADMIN_60 = "192.168.60.100/32"
ADMIN_61 = "192.168.61.100/32"
ADMIN_62 = "192.168.62.100/32"
ADMIN_63 = "192.168.63.100/32"
ADMIN_64 = "192.168.64.100/32"
ADMIN_65 = "192.168.65.100/32"
ADMIN_66 = "192.168.66.100/32"
ADMIN_67 = "192.168.67.100/32"
ADMIN_68 = "192.168.68.100/32"
ADMIN_69 = "192.168.69.100/32"
ADMIN_70 = "192.168.70.100/32"
ADMIN_71 = "192.168.71.100/32"
ADMIN_72 = "192.168.72.100/32"
ADMIN_73 = "192.168.73.100/32"
ADMIN_74 = "192.168.74.100/32"
ADMIN_75 = "192.168.75.100/32"
ADMIN_76 = "192.168.76.100/32"
ADMIN_77 = "192.168.77.100/32"
ADMIN_78 = "192.168.78.100/32"
ADMIN_79 = "192.168.79.100/32"
ADMIN_80 = "192.168.80.100/32"
ADMIN_81 = "192.168.81.100/32"
ADMIN_82 = "192.168.82.100/32"
ADMIN_83 = "192.168.83.100/32"
ADMIN_84 = "192.168.84.100/32"
ADMIN_85 = "192.168.85.100/32"
ADMIN_86 = "192.168.86.100/32"
ADMIN_87 = "192.168.87.100/32"
ADMIN_88 = "192.168.88.100/32"
ADMIN_89 = "192.168.89.100/32"
ADMIN_90 = "192.168.90.100/32"
ADMIN_91 = "192.168.91.100/32"
ADMIN_92 = "192.168.92.100/32"
ADMIN_93 = "192.168.93.100/32"
ADMIN_94 = "192.168.94.100/32"
ADMIN_95 = "192.168.95.100/32"
ADMIN_96 = "192.168.96.100/32"
ADMIN_97 = "192.168.97.100/32"
ADMIN_98 = "192.168.98.100/32"
ADMIN_99 = "192.168.99.100/32"

RZONE = "192.168.0.100/28"

FUNCTIONS_AND_LOCATIONS = {}
LABELS = {}
IP_LOCATIONS = {}

FUNCTIONS_AND_LOCATIONS["FW"] = [0,1,2]
FUNCTIONS_AND_LOCATIONS["COUNTER"] = [3,7,12]
#FUNCTIONS_AND_LOCATIONS["FW2"] = [20,21,22]
#FUNCTIONS_AND_LOCATIONS["COUNTER2"] = [30,31,32]


FUNCTIONS_AND_LOCATIONS["SPECIAL_COUNTER"] = [7]

LABELS["Zones"] = [ZONE_0,ZONE_1,ZONE_2,ZONE_3,ZONE_4,ZONE_5,ZONE_6,ZONE_7,ZONE_8,ZONE_9,ZONE_10,ZONE_11,ZONE_12,ZONE_13,ZONE_14,ZONE_15,ZONE_16,ZONE_17,ZONE_18,ZONE_19,ZONE_20,ZONE_21,ZONE_22,ZONE_23,ZONE_24,ZONE_25,ZONE_26,ZONE_27,ZONE_28,ZONE_29,ZONE_30,ZONE_31,ZONE_32,ZONE_33,ZONE_34,ZONE_35,ZONE_36,ZONE_37,ZONE_38,ZONE_39,ZONE_40,ZONE_41,ZONE_42,ZONE_43,ZONE_44,ZONE_45,ZONE_46,ZONE_47,ZONE_48,ZONE_49,ZONE_50,ZONE_51,ZONE_52,ZONE_53,ZONE_54,ZONE_55,ZONE_56,ZONE_57,ZONE_58,ZONE_59,ZONE_60,ZONE_61,ZONE_62,ZONE_63,ZONE_64,ZONE_65,ZONE_66,ZONE_67,ZONE_68,ZONE_69,ZONE_70,ZONE_71,ZONE_72,ZONE_73,ZONE_74,ZONE_75,ZONE_76,ZONE_77,ZONE_78,ZONE_79,ZONE_80,ZONE_81,ZONE_82,ZONE_83,ZONE_84,ZONE_85,ZONE_86,ZONE_87,ZONE_88,ZONE_89,ZONE_90,ZONE_91,ZONE_92,ZONE_93,ZONE_94,ZONE_95,ZONE_96,ZONE_97,ZONE_98,ZONE_99]
LABELS["Admins"] = [ADMIN_0,ADMIN_1,ADMIN_2,ADMIN_3,ADMIN_4,ADMIN_5,ADMIN_6,ADMIN_7,ADMIN_8,ADMIN_9,ADMIN_10,ADMIN_11,ADMIN_12,ADMIN_13,ADMIN_14,ADMIN_15,ADMIN_16,ADMIN_17,ADMIN_18,ADMIN_19,ADMIN_20,ADMIN_21,ADMIN_22,ADMIN_23,ADMIN_24,ADMIN_25,ADMIN_26,ADMIN_27,ADMIN_28,ADMIN_29,ADMIN_30,ADMIN_31,ADMIN_32,ADMIN_33,ADMIN_34,ADMIN_35,ADMIN_36,ADMIN_37,ADMIN_38,ADMIN_39,ADMIN_40,ADMIN_41,ADMIN_42,ADMIN_43,ADMIN_44,ADMIN_45,ADMIN_46,ADMIN_47,ADMIN_48,ADMIN_49,ADMIN_50,ADMIN_51,ADMIN_52,ADMIN_53,ADMIN_54,ADMIN_55,ADMIN_56,ADMIN_57,ADMIN_58,ADMIN_59,ADMIN_60,ADMIN_61,ADMIN_62,ADMIN_63,ADMIN_64,ADMIN_65,ADMIN_66,ADMIN_67,ADMIN_68,ADMIN_69,ADMIN_70,ADMIN_71,ADMIN_72,ADMIN_73,ADMIN_74,ADMIN_75,ADMIN_76,ADMIN_77,ADMIN_78,ADMIN_79,ADMIN_80,ADMIN_81,ADMIN_82,ADMIN_83,ADMIN_84,ADMIN_85,ADMIN_86,ADMIN_87,ADMIN_88,ADMIN_89,ADMIN_90,ADMIN_91,ADMIN_92,ADMIN_93,ADMIN_94,ADMIN_95,ADMIN_96,ADMIN_97,ADMIN_98,ADMIN_99]
LABELS["SpecialAdmins"] = [ADMIN_0]
LABELS["rZone"] = [RZONE]

LABELS["Broadcast"] = [BROADCAST_IP] 
LABELS["Broadcast2"] = [BROADCAST2_IP] 

IP_LOCATIONS[ZONE_0] = 0
IP_LOCATIONS[ZONE_1] = 1
IP_LOCATIONS[ZONE_2] = 2
IP_LOCATIONS[ZONE_3] = 3
IP_LOCATIONS[ZONE_4] = 4
IP_LOCATIONS[ZONE_5] = 5
IP_LOCATIONS[ZONE_6] = 6
IP_LOCATIONS[ZONE_7] = 7
IP_LOCATIONS[ZONE_8] = 8
IP_LOCATIONS[ZONE_9] = 9
IP_LOCATIONS[ZONE_10] = 10
IP_LOCATIONS[ZONE_11] = 11
IP_LOCATIONS[ZONE_12] = 12
IP_LOCATIONS[ZONE_13] = 13
IP_LOCATIONS[ZONE_14] = 14
IP_LOCATIONS[ZONE_15] = 15
IP_LOCATIONS[ZONE_16] = 16
IP_LOCATIONS[ZONE_17] = 17
IP_LOCATIONS[ZONE_18] = 18
IP_LOCATIONS[ZONE_19] = 19
IP_LOCATIONS[ZONE_20] = 20
IP_LOCATIONS[ZONE_21] = 21
IP_LOCATIONS[ZONE_22] = 22
IP_LOCATIONS[ZONE_23] = 23
IP_LOCATIONS[ZONE_24] = 24
IP_LOCATIONS[ZONE_25] = 0
IP_LOCATIONS[ZONE_26] = 1
IP_LOCATIONS[ZONE_27] = 2
IP_LOCATIONS[ZONE_28] = 3
IP_LOCATIONS[ZONE_29] = 4
IP_LOCATIONS[ZONE_30] = 5
IP_LOCATIONS[ZONE_31] = 6
IP_LOCATIONS[ZONE_32] = 7
IP_LOCATIONS[ZONE_33] = 8
IP_LOCATIONS[ZONE_34] = 9
IP_LOCATIONS[ZONE_35] = 10
IP_LOCATIONS[ZONE_36] = 11
IP_LOCATIONS[ZONE_37] = 12
IP_LOCATIONS[ZONE_38] = 13
IP_LOCATIONS[ZONE_39] = 14
IP_LOCATIONS[ZONE_40] = 15
IP_LOCATIONS[ZONE_41] = 16
IP_LOCATIONS[ZONE_42] = 17
IP_LOCATIONS[ZONE_43] = 18
IP_LOCATIONS[ZONE_44] = 19
IP_LOCATIONS[ZONE_45] = 20
IP_LOCATIONS[ZONE_46] = 21
IP_LOCATIONS[ZONE_47] = 22
IP_LOCATIONS[ZONE_48] = 23
IP_LOCATIONS[ZONE_49] = 24
IP_LOCATIONS[ZONE_50] = 0
IP_LOCATIONS[ZONE_51] = 1
IP_LOCATIONS[ZONE_52] = 2
IP_LOCATIONS[ZONE_53] = 3
IP_LOCATIONS[ZONE_54] = 4
IP_LOCATIONS[ZONE_55] = 5
IP_LOCATIONS[ZONE_56] = 6
IP_LOCATIONS[ZONE_57] = 7
IP_LOCATIONS[ZONE_58] = 8
IP_LOCATIONS[ZONE_59] = 9
IP_LOCATIONS[ZONE_60] = 10
IP_LOCATIONS[ZONE_61] = 11
IP_LOCATIONS[ZONE_62] = 12
IP_LOCATIONS[ZONE_63] = 13
IP_LOCATIONS[ZONE_64] = 14
IP_LOCATIONS[ZONE_65] = 15
IP_LOCATIONS[ZONE_66] = 16
IP_LOCATIONS[ZONE_67] = 17
IP_LOCATIONS[ZONE_68] = 18
IP_LOCATIONS[ZONE_69] = 19
IP_LOCATIONS[ZONE_70] = 20
IP_LOCATIONS[ZONE_71] = 21
IP_LOCATIONS[ZONE_72] = 22
IP_LOCATIONS[ZONE_73] = 23
IP_LOCATIONS[ZONE_74] = 24
IP_LOCATIONS[ZONE_75] = 0
IP_LOCATIONS[ZONE_76] = 1
IP_LOCATIONS[ZONE_77] = 2
IP_LOCATIONS[ZONE_78] = 3
IP_LOCATIONS[ZONE_79] = 4
IP_LOCATIONS[ZONE_80] = 5
IP_LOCATIONS[ZONE_81] = 6
IP_LOCATIONS[ZONE_82] = 7
IP_LOCATIONS[ZONE_83] = 8
IP_LOCATIONS[ZONE_84] = 9
IP_LOCATIONS[ZONE_85] = 10
IP_LOCATIONS[ZONE_86] = 11
IP_LOCATIONS[ZONE_87] = 12
IP_LOCATIONS[ZONE_88] = 13
IP_LOCATIONS[ZONE_89] = 14
IP_LOCATIONS[ZONE_90] = 15
IP_LOCATIONS[ZONE_91] = 16
IP_LOCATIONS[ZONE_92] = 17
IP_LOCATIONS[ZONE_93] = 18
IP_LOCATIONS[ZONE_94] = 19
IP_LOCATIONS[ZONE_95] = 20
IP_LOCATIONS[ZONE_96] = 21
IP_LOCATIONS[ZONE_97] = 22
IP_LOCATIONS[ZONE_98] = 23
IP_LOCATIONS[ZONE_99] = 24

IP_LOCATIONS[BROADCAST_IP] = 25
IP_LOCATIONS[BROADCAST2_IP] = 25


POLICIES = []
POLICIES.append("*:Broadcast->FW->Zones")
POLICIES.append("dst_port=80:Broadcast->COUNTER->Admins")
#POLICIES.append("*:Broadcast2->FW2->Zones")
#POLICIES.append("dst_port=1433:Broadcast2->COUNTER2->Admins")
#POLICIES.append("*:Broadcast->FW->rZone")

ADDITIONAL_POLICIES = []
ADDITIONAL_POLICIES.append("dst_port=80:!Broadcast->SPECIAL_COUNTER->SpecialAdmins")