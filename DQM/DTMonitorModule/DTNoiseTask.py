import FWCore.ParameterSet.Config as cms

def DTNoiseTask(**kwargs):
  mod = cms.EDProducer('DTNoiseTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
