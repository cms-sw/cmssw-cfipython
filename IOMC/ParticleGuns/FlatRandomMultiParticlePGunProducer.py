import FWCore.ParameterSet.Config as cms

def FlatRandomMultiParticlePGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FlatRandomMultiParticlePGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
