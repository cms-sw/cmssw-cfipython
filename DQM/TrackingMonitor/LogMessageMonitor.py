import FWCore.ParameterSet.Config as cms

def LogMessageMonitor(*args, **kwargs):
  mod = cms.EDProducer('LogMessageMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
