import FWCore.ParameterSet.Config as cms

def EERecHitGPU(*args, **kwargs):
  mod = cms.EDProducer('EERecHitGPU',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
