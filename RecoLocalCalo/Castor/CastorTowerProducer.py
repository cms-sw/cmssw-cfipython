import FWCore.ParameterSet.Config as cms

def CastorTowerProducer(**kwargs):
  mod = cms.EDProducer('CastorTowerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
