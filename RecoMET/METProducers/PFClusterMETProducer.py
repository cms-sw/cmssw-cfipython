import FWCore.ParameterSet.Config as cms

def PFClusterMETProducer(**kwargs):
  mod = cms.EDProducer('PFClusterMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
