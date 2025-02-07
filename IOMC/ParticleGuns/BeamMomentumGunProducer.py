import FWCore.ParameterSet.Config as cms

def BeamMomentumGunProducer(*args, **kwargs):
  mod = cms.EDProducer('BeamMomentumGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
