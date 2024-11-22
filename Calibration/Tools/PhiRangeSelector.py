import FWCore.ParameterSet.Config as cms

def PhiRangeSelector(*args, **kwargs):
  mod = cms.EDFilter('PhiRangeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
