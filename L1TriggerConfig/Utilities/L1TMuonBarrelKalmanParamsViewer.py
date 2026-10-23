import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelKalmanParamsViewer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TMuonBarrelKalmanParamsViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
