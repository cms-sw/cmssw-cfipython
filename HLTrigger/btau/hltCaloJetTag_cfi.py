import FWCore.ParameterSet.Config as cms

hltCaloJetTag = cms.EDFilter('HLTCaloJetTag',
  saveTags = cms.bool(True),
  Jets = cms.InputTag('hltJetCollection'),
  JetTags = cms.InputTag('hltJetTagCollection'),
  MinTag = cms.double(2),
  MaxTag = cms.double(999999),
  MinJets = cms.int32(1),
  MatchJetsByDeltaR = cms.bool(False),
  MaxJetDeltaR = cms.double(0.1),
  TriggerType = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)