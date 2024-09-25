import FWCore.ParameterSet.Config as cms

def HcalRawToDigiGPU(*args, **kwargs):
  mod = cms.EDProducer('HcalRawToDigiGPU',
    InputLabel = cms.InputTag('rawDataCollector'),
    FEDs = cms.vint32(
      1100,
      1101,
      1102,
      1103,
      1104,
      1105,
      1106,
      1107,
      1108,
      1109,
      1110,
      1111,
      1112,
      1113,
      1114,
      1115,
      1116,
      1117,
      1118,
      1119,
      1120,
      1121,
      1122,
      1123,
      1124,
      1125,
      1126,
      1127,
      1128,
      1129,
      1130,
      1131,
      1132,
      1133,
      1134,
      1135,
      1136,
      1137,
      1138,
      1139,
      1140,
      1141,
      1142,
      1143,
      1144,
      1145,
      1146,
      1147,
      1148,
      1149,
      1150,
      1151,
      1152,
      1153,
      1154,
      1155,
      1156,
      1157,
      1158,
      1159,
      1160,
      1161,
      1162,
      1163,
      1164,
      1165,
      1166,
      1167,
      1168,
      1169,
      1170,
      1171,
      1172,
      1173,
      1174,
      1175,
      1176,
      1177,
      1178,
      1179,
      1180,
      1181,
      1182,
      1183,
      1184,
      1185,
      1186,
      1187,
      1188,
      1189,
      1190,
      1191,
      1192,
      1193,
      1194,
      1195,
      1196,
      1197,
      1198,
      1199
    ),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    nsamplesF01HE = cms.uint32(8),
    nsamplesF5HB = cms.uint32(8),
    nsamplesF3HB = cms.uint32(8),
    digisLabelF5HB = cms.string('f5HBDigisGPU'),
    digisLabelF01HE = cms.string('f01HEDigisGPU'),
    digisLabelF3HB = cms.string('f3HBDigisGPU'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
