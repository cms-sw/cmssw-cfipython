import FWCore.ParameterSet.Config as cms

def HEFRecHitGPU(*args, **kwargs):
  mod = cms.EDProducer('HEFRecHitGPU',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
