import FWCore.ParameterSet.Config as cms

def HFPhase1PMTParamsDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HFPhase1PMTParamsDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
