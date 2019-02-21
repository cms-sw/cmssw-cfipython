import FWCore.ParameterSet.Config as cms

hlt2jetGapFilter = cms.EDFilter('HLT2jetGapFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('iterativeCone5CaloJets'),
  minEt = cms.double(90),
  minEta = cms.double(1.9)
)
