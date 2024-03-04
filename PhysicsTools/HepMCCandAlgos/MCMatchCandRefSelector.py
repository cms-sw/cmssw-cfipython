import FWCore.ParameterSet.Config as cms

def MCMatchCandRefSelector(**kwargs):
  mod = cms.EDFilter('MCMatchCandRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
