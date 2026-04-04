import FWCore.ParameterSet.Config as cms

def UTC_SLUMMARY(*args, **kwargs):
  mod = cms.EDAnalyzer('UTC_SLUMMARY',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
