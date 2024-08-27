import FWCore.ParameterSet.Config as cms

def RawTask(**kwargs):
  mod = cms.EDProducer('RawTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
