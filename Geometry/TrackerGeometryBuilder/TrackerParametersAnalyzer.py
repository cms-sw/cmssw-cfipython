import FWCore.ParameterSet.Config as cms

def TrackerParametersAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackerParametersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
