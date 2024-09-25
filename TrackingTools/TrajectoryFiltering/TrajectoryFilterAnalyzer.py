import FWCore.ParameterSet.Config as cms

def TrajectoryFilterAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrajectoryFilterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
