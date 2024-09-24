import FWCore.ParameterSet.Config as cms

def PATHeavyIonProducer(*args, **kwargs):
  mod = cms.EDProducer('PATHeavyIonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
