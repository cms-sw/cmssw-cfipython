import FWCore.ParameterSet.Config as cms

triggerRatesMonitor = cms.EDAnalyzer('TriggerRatesMonitor',
  l1tResults = cms.untracked.InputTag('gtStage2Digis'),
  hltResults = cms.untracked.InputTag('TriggerResults'),
  dqmPath = cms.untracked.string('HLT/TriggerRates'),
  lumisectionRange = cms.untracked.uint32(2500)
)
