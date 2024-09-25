import FWCore.ParameterSet.Config as cms

def TestTrackerHierarchy(*args, **kwargs):
  mod = cms.EDAnalyzer('TestTrackerHierarchy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
