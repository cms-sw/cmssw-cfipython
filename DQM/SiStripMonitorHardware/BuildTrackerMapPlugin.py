import FWCore.ParameterSet.Config as cms

def BuildTrackerMapPlugin(*args, **kwargs):
  mod = cms.EDAnalyzer('BuildTrackerMapPlugin',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
