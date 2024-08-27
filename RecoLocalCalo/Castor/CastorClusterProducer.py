import FWCore.ParameterSet.Config as cms

def CastorClusterProducer(**kwargs):
  mod = cms.EDProducer('CastorClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
