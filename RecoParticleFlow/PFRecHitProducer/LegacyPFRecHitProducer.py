import FWCore.ParameterSet.Config as cms

def LegacyPFRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('LegacyPFRecHitProducer',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
