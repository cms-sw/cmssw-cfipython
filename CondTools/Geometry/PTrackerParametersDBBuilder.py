import FWCore.ParameterSet.Config as cms

def PTrackerParametersDBBuilder(**kwargs):
  mod = cms.EDAnalyzer('PTrackerParametersDBBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
