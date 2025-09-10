import FWCore.ParameterSet.Config as cms

def SherpaGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('SherpaGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
