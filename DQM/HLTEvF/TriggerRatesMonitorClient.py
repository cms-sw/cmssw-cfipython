import FWCore.ParameterSet.Config as cms

def TriggerRatesMonitorClient(*args, **kwargs):
  mod = cms.EDProducer('TriggerRatesMonitorClient',
    dqmPath = cms.untracked.string('HLT/Datasets'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
