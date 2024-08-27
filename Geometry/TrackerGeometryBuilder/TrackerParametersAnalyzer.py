import FWCore.ParameterSet.Config as cms

def TrackerParametersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackerParametersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
