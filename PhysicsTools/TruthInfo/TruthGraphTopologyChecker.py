import FWCore.ParameterSet.Config as cms

def TruthGraphTopologyChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('TruthGraphTopologyChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
