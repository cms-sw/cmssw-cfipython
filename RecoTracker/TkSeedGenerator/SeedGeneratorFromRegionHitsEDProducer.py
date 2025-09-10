import FWCore.ParameterSet.Config as cms

def SeedGeneratorFromRegionHitsEDProducer(*args, **kwargs):
  mod = cms.EDProducer('SeedGeneratorFromRegionHitsEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
