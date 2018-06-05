import FWCore.ParameterSet.Config as cms

hltNVFilter = cms.EDFilter('HLTNVFilter',
  saveTags = cms.bool(True),
  inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
  inputMETTag = cms.InputTag('hlt1MET60'),
  minEtJet2 = cms.double(20),
  minEtJet1 = cms.double(80),
  minNV = cms.double(0.1)
)
