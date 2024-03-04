import FWCore.ParameterSet.Config as cms

def HLXMonitor(**kwargs):
  mod = cms.EDProducer('HLXMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
