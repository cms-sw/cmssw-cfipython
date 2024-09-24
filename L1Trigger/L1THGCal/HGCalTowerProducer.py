import FWCore.ParameterSet.Config as cms

def HGCalTowerProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalTowerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
