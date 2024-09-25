import FWCore.ParameterSet.Config as cms

def RandomXiThetaGunProducer(*args, **kwargs):
  mod = cms.EDProducer('RandomXiThetaGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
