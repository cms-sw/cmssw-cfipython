import FWCore.ParameterSet.Config as cms

hltHcalTowerFilter = cms.EDFilter('HLTHcalTowerFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltTowerMakerForHcal'),
  MinE_HB = cms.double(1.5),
  MinE_HE = cms.double(2.5),
  MinE_HF = cms.double(9),
  MaxN_HB = cms.int32(2),
  MaxN_HE = cms.int32(2),
  MaxN_HF = cms.int32(8),
  MinN_HF = cms.int32(-1),
  MinN_HFM = cms.int32(-1),
  MinN_HFP = cms.int32(-1)
)
