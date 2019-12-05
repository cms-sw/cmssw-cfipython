import FWCore.ParameterSet.Config as cms

hlt9HLTJetTagIN4reco7CaloJetEE = cms.EDFilter('HLTCaloJetTag',
  saveTags = cms.bool(False),
  Jets = cms.InputTag('hltJetCollection'),
  JetTags = cms.InputTag('hltJetTagCollection'),
  MinTag = cms.double(2),
  MaxTag = cms.double(999999),
  MinJets = cms.int32(1),
  TriggerType = cms.int32(0)
)
