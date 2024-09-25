import FWCore.ParameterSet.Config as cms

def PtMinCandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
