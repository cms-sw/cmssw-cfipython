import FWCore.ParameterSet.Config as cms

def TopDecaySubset(**kwargs):
  mod = cms.EDProducer('TopDecaySubset',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
