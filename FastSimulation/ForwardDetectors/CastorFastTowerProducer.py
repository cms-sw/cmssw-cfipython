import FWCore.ParameterSet.Config as cms

def CastorFastTowerProducer(**kwargs):
  mod = cms.EDProducer('CastorFastTowerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
