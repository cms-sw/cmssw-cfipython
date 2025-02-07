import FWCore.ParameterSet.Config as cms

def HijingGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('HijingGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
