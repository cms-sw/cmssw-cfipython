import FWCore.ParameterSet.Config as cms

def TriggerMatchMonitor(**kwargs):
  mod = cms.EDProducer('TriggerMatchMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
