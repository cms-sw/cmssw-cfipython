import FWCore.ParameterSet.Config as cms

def HLTDTActivityFilter(**kwargs):
  mod = cms.EDFilter('HLTDTActivityFilter',
    saveTags = cms.bool(True),
    inputDCC = cms.InputTag('hltDTTFUnpacker'),
    inputDDU = cms.InputTag('hltMuonDTDigis'),
    inputRPC = cms.InputTag('hltGtDigis'),
    inputDigis = cms.InputTag('hltMuonDTDigis'),
    processDCC = cms.bool(True),
    processDDU = cms.bool(True),
    processRPC = cms.bool(True),
    processDigis = cms.bool(True),
    orTPG = cms.bool(True),
    orRPC = cms.bool(True),
    orDigi = cms.bool(False),
    minDCCBX = cms.int32(-1),
    maxDCCBX = cms.int32(1),
    minDDUBX = cms.int32(8),
    maxDDUBX = cms.int32(13),
    minRPCBX = cms.int32(-1),
    maxRPCBX = cms.int32(1),
    minTPGQual = cms.int32(2),
    maxStation = cms.int32(3),
    minChamberLayers = cms.int32(5),
    minActiveChambs = cms.int32(1),
    MaxDeltaPhi = cms.double(1),
    MaxDeltaEta = cms.double(0.3),
    activeSectors = cms.vint32(
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
