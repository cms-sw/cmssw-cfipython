import FWCore.ParameterSet.Config as cms

def RecHitTask(**kwargs):
  mod = cms.EDProducer('RecHitTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
