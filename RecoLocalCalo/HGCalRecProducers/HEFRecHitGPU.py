import FWCore.ParameterSet.Config as cms

def HEFRecHitGPU(**kwargs):
  mod = cms.EDProducer('HEFRecHitGPU',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
