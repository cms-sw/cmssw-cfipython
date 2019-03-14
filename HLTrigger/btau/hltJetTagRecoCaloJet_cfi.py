import FWCore.ParameterSet.Config as cms

hltJetTagRecoCaloJet = cms.EDFilter('HLTCaloJetTag',
  saveTags = cms.bool(True),
  Jets = cms.InputTag('hltJetCollection'),
  JetTags = cms.InputTag('hltJetTagCollection'),
  MinTag = cms.double(2),
  MaxTag = cms.double(999999),
  MinJets = cms.int32(1),
  TriggerType = cms.int32(0)
)
