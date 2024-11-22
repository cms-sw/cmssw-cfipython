import FWCore.ParameterSet.Config as cms

def CandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('CandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
