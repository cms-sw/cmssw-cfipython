import FWCore.ParameterSet.Config as cms

def PFClusterTimeSelector(**kwargs):
  mod = cms.EDProducer('PFClusterTimeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
