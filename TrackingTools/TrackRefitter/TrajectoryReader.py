import FWCore.ParameterSet.Config as cms

def TrajectoryReader(**kwargs):
  mod = cms.EDAnalyzer('TrajectoryReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
