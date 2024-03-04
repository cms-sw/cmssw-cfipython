import FWCore.ParameterSet.Config as cms

def PFClusterProducer(**kwargs):
  mod = cms.EDProducer('PFClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
