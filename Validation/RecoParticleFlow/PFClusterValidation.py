import FWCore.ParameterSet.Config as cms

def PFClusterValidation(**kwargs):
  mod = cms.EDProducer('PFClusterValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
