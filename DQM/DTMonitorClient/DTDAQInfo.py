import FWCore.ParameterSet.Config as cms

def DTDAQInfo(**kwargs):
  mod = cms.EDProducer('DTDAQInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
