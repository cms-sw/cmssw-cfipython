import FWCore.ParameterSet.Config as cms

L1TriggerJSONMonitoring = cms.EDAnalyzer('L1TriggerJSONMonitoring',
  L1Results = cms.InputTag('hltGtStage2Digis')
)
