import FWCore.ParameterSet.Config as cms

def TestTrackerHierarchy(**kwargs):
  mod = cms.EDAnalyzer('TestTrackerHierarchy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
