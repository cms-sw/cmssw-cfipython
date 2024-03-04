import FWCore.ParameterSet.Config as cms

def TrajectoryFilterAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrajectoryFilterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
