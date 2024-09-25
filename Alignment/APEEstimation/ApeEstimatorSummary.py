import FWCore.ParameterSet.Config as cms

def ApeEstimatorSummary(*args, **kwargs):
  mod = cms.EDAnalyzer('ApeEstimatorSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
