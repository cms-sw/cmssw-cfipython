import FWCore.ParameterSet.Config as cms

HLTriggerJSONMonitoring = cms.EDAnalyzer('HLTriggerJSONMonitoring',
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT')
)
