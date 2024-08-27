import FWCore.ParameterSet.Config as cms

def RCTMonitor(**kwargs):
  mod = cms.EDProducer('RCTMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
