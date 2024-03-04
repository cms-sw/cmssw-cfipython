import FWCore.ParameterSet.Config as cms

def BuildTrackerMapPlugin(**kwargs):
  mod = cms.EDAnalyzer('BuildTrackerMapPlugin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
