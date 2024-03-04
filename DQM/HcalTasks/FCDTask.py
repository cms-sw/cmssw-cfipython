import FWCore.ParameterSet.Config as cms

def FCDTask(**kwargs):
  mod = cms.EDProducer('FCDTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
