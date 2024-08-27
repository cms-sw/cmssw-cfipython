import FWCore.ParameterSet.Config as cms

def DTClusterer(**kwargs):
  mod = cms.EDProducer('DTClusterer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
