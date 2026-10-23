import FWCore.ParameterSet.Config as cms

def TrajectoryCleanerAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrajectoryCleanerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
