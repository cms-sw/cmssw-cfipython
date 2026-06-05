import FWCore.ParameterSet.Config as cms

def Phase2TrackerFEDTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerFEDTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
