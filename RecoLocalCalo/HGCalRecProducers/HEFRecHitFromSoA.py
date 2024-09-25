import FWCore.ParameterSet.Config as cms

def HEFRecHitFromSoA(*args, **kwargs):
  mod = cms.EDProducer('HEFRecHitFromSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
