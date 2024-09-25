import FWCore.ParameterSet.Config as cms

def RecoCandViewRefSelector(*args, **kwargs):
  mod = cms.EDFilter('RecoCandViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
