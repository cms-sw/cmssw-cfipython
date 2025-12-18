import FWCore.ParameterSet.Config as cms

def FlatRandomPtThetaGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FlatRandomPtThetaGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
