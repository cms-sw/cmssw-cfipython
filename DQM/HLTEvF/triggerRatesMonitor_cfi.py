import FWCore.ParameterSet.Config as cms

triggerRatesMonitor = cms.EDProducer('TriggerRatesMonitor',
  l1tResults = cms.untracked.InputTag('gtStage2Digis'),
  hltResults = cms.untracked.InputTag('TriggerResults'),
  dqmPath = cms.untracked.string('HLT/TriggerRates'),
  lumisectionRange = cms.untracked.uint32(2500),
  mightGet = cms.optional.untracked.vstring
)
