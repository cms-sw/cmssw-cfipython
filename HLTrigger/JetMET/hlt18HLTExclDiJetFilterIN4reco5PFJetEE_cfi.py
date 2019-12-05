import FWCore.ParameterSet.Config as cms

hlt18HLTExclDiJetFilterIN4reco5PFJetEE = cms.EDFilter('HLTExclDiPFJetFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minPtJet = cms.double(30),
  minHFe = cms.double(50),
  HF_OR = cms.bool(False),
  triggerType = cms.int32(85)
)
