import FWCore.ParameterSet.Config as cms

def ReggeGribovPartonMCGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('ReggeGribovPartonMCGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
