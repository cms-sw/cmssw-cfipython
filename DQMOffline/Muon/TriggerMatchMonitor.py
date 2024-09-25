import FWCore.ParameterSet.Config as cms

def TriggerMatchMonitor(*args, **kwargs):
  mod = cms.EDProducer('TriggerMatchMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
