import FWCore.ParameterSet.Config as cms

def HGCalTowerMapProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalTowerMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
