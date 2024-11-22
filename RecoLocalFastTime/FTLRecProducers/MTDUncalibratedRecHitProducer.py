import FWCore.ParameterSet.Config as cms

def MTDUncalibratedRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDUncalibratedRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
