import FWCore.ParameterSet.Config as cms

def LogMessageMonitor(**kwargs):
  mod = cms.EDProducer('LogMessageMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
