import FWCore.ParameterSet.Config as cms

def PTrackerAdditionalParametersPerDetDBBuilder(**kwargs):
  mod = cms.EDAnalyzer('PTrackerAdditionalParametersPerDetDBBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
