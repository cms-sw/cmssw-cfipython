import FWCore.ParameterSet.Config as cms

triggerBxVsOrbitMonitor = cms.EDAnalyzer('TriggerBxVsOrbitMonitor',
  l1tResults = cms.untracked.InputTag('gtStage2Digis'),
  hltResults = cms.untracked.InputTag('TriggerResults'),
  dqmPath = cms.untracked.string('HLT/TriggerBx')
)
