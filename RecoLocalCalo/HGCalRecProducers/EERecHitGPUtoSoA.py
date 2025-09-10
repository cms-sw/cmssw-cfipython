import FWCore.ParameterSet.Config as cms

def EERecHitGPUtoSoA(*args, **kwargs):
  mod = cms.EDProducer('EERecHitGPUtoSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
