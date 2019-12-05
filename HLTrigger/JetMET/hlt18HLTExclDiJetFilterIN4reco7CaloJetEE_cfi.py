import FWCore.ParameterSet.Config as cms

hlt18HLTExclDiJetFilterIN4reco7CaloJetEE = cms.EDFilter('HLTExclDiCaloJetFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minPtJet = cms.double(30),
  minHFe = cms.double(50),
  HF_OR = cms.bool(False),
  triggerType = cms.int32(85)
)
