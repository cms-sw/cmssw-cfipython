import FWCore.ParameterSet.Config as cms

hltEcalTowerFilter = cms.EDFilter('HLTEcalTowerFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltTowerMakerForEcal'),
  MinE = cms.double(10),
  MaxEta = cms.double(3),
  MinN = cms.int32(1)
)
