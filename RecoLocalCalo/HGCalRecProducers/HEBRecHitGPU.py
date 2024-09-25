import FWCore.ParameterSet.Config as cms

def HEBRecHitGPU(*args, **kwargs):
  mod = cms.EDProducer('HEBRecHitGPU',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
