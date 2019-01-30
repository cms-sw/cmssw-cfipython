import FWCore.ParameterSet.Config as cms

triggerJSONMonitoring = cms.EDAnalyzer('TriggerJSONMonitoring',
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT')
)
