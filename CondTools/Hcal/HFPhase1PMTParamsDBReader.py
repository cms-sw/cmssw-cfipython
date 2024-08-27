import FWCore.ParameterSet.Config as cms

def HFPhase1PMTParamsDBReader(**kwargs):
  mod = cms.EDAnalyzer('HFPhase1PMTParamsDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
