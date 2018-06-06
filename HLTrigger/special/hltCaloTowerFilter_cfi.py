import FWCore.ParameterSet.Config as cms

hltCaloTowerFilter = cms.EDFilter('HLTCaloTowerFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltTowerMakerForEcal'),
  MinPt = cms.double(3),
  MaxEta = cms.double(3),
  MinN = cms.uint32(1)
)
