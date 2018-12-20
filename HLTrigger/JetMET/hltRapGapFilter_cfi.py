import FWCore.ParameterSet.Config as cms

hltRapGapFilter = cms.EDFilter('HLTRapGapFilter',
  saveTags = cms.bool(True),
  inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
  minEta = cms.double(3),
  maxEta = cms.double(5),
  caloThresh = cms.double(20)
)
