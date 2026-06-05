import FWCore.ParameterSet.Config as cms

def ApeEstimator(*args, **kwargs):
  mod = cms.EDAnalyzer('ApeEstimator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
