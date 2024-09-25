import FWCore.ParameterSet.Config as cms

def MCMatchCandRefSelector(*args, **kwargs):
  mod = cms.EDFilter('MCMatchCandRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
