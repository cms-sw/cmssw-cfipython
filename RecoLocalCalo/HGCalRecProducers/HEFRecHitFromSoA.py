import FWCore.ParameterSet.Config as cms

def HEFRecHitFromSoA(**kwargs):
  mod = cms.EDProducer('HEFRecHitFromSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
