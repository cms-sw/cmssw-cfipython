import FWCore.ParameterSet.Config as cms

def StatusCandSelector(*args, **kwargs):
  mod = cms.EDFilter('StatusCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
