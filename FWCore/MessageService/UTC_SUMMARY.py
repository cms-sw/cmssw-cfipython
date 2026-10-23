import FWCore.ParameterSet.Config as cms

def UTC_SUMMARY(*args, **kwargs):
  mod = cms.EDAnalyzer('UTC_SUMMARY',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
