import FWCore.ParameterSet.Config as cms

def Phase2TrackerFEDTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerFEDTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
