import FWCore.ParameterSet.Config as cms

def PyquenGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('PyquenGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
