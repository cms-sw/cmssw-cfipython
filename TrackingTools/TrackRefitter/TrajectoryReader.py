import FWCore.ParameterSet.Config as cms

def TrajectoryReader(*args, **kwargs):
  mod = cms.EDAnalyzer('TrajectoryReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
