import FWCore.ParameterSet.Config as cms

def HGCalTowerProducer(**kwargs):
  mod = cms.EDProducer('HGCalTowerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
