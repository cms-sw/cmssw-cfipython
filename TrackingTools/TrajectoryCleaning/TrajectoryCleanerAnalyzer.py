import FWCore.ParameterSet.Config as cms

def TrajectoryCleanerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrajectoryCleanerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
