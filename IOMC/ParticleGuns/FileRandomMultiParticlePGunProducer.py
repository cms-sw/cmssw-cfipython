import FWCore.ParameterSet.Config as cms

def FileRandomMultiParticlePGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FileRandomMultiParticlePGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
