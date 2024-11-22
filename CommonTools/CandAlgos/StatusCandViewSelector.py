import FWCore.ParameterSet.Config as cms

def StatusCandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('StatusCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
