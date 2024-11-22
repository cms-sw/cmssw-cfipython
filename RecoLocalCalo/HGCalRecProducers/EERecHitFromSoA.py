import FWCore.ParameterSet.Config as cms

def EERecHitFromSoA(*args, **kwargs):
  mod = cms.EDProducer('EERecHitFromSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
