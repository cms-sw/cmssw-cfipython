import FWCore.ParameterSet.Config as cms

def TPTask(**kwargs):
  mod = cms.EDProducer('TPTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
