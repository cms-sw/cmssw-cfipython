import FWCore.ParameterSet.Config as cms

def TestInterProcessRandomProd(**kwargs):
  mod = cms.EDProducer('TestInterProcessRandomProd',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
