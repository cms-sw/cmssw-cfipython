import FWCore.ParameterSet.Config as cms

def L1GlobalTrigger(**kwargs):
  mod = cms.EDProducer('L1GlobalTrigger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
