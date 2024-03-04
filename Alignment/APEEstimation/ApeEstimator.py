import FWCore.ParameterSet.Config as cms

def ApeEstimator(**kwargs):
  mod = cms.EDAnalyzer('ApeEstimator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
