import FWCore.ParameterSet.Config as cms

def TriggerRatesMonitor(*args, **kwargs):
  mod = cms.EDProducer('TriggerRatesMonitor',
    l1tResults = cms.untracked.InputTag('gtStage2Digis'),
    hltResults = cms.untracked.InputTag('TriggerResults'),
    dqmPath = cms.untracked.string('HLT/TriggerRates'),
    lumisectionRange = cms.untracked.uint32(2500),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
