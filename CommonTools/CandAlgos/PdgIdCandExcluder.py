import FWCore.ParameterSet.Config as cms

def PdgIdCandExcluder(*args, **kwargs):
  mod = cms.EDFilter('PdgIdCandExcluder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
