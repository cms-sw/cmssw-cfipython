import FWCore.ParameterSet.Config as cms

def FileRandomKEThetaGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FileRandomKEThetaGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
