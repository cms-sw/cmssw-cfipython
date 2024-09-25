import FWCore.ParameterSet.Config as cms

def EcalDetailedTimeRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalDetailedTimeRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
