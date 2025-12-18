import FWCore.ParameterSet.Config as cms

def HFPhase1PMTParamsDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('HFPhase1PMTParamsDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
