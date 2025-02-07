import FWCore.ParameterSet.Config as cms

def HEBRecHitGPUtoSoA(*args, **kwargs):
  mod = cms.EDProducer('HEBRecHitGPUtoSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
