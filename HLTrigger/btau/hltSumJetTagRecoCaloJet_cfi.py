import FWCore.ParameterSet.Config as cms

hltSumJetTagRecoCaloJet = cms.EDFilter('HLTSumCaloJetTag',
  saveTags = cms.bool(True),
  Jets = cms.InputTag('hltJetCollection'),
  JetTags = cms.InputTag('hltJetTagCollection'),
  MinTag = cms.double(0),
  MaxTag = cms.double(999999),
  MinJetToSum = cms.int32(1),
  MaxJetToSum = cms.int32(99),
  UseMeanValue = cms.bool(True),
  MatchByDeltaR = cms.bool(False),
  MaxDeltaR = cms.double(0.4),
  TriggerType = cms.int32(86),
  mightGet = cms.optional.untracked.vstring
)
