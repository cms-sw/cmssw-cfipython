import FWCore.ParameterSet.Config as cms

def PdgIdAndStatusCandSelector(*args, **kwargs):
  mod = cms.EDFilter('PdgIdAndStatusCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
