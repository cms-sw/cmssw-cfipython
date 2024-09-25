import FWCore.ParameterSet.Config as cms

def EcalRecalibRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalRecalibRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
