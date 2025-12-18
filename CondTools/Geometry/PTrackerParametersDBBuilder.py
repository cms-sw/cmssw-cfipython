import FWCore.ParameterSet.Config as cms

def PTrackerParametersDBBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('PTrackerParametersDBBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
