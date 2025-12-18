import FWCore.ParameterSet.Config as cms

def EcalRecHitColCleaner(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
