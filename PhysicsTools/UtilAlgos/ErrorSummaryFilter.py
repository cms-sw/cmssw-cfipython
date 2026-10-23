import FWCore.ParameterSet.Config as cms

def ErrorSummaryFilter(*args, **kwargs):
  mod = cms.EDFilter('ErrorSummaryFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
