import FWCore.ParameterSet.Config as cms

def DTTrigProd(**kwargs):
  mod = cms.EDProducer('DTTrigProd',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
