import FWCore.ParameterSet.Config as cms

def HGCalTowerMapProducer(**kwargs):
  mod = cms.EDProducer('HGCalTowerMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
