import FWCore.ParameterSet.Config as cms

def HGCalRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
