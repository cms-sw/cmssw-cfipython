import FWCore.ParameterSet.Config as cms

def EcalRecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
