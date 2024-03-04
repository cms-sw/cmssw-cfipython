import FWCore.ParameterSet.Config as cms

def HFPhase1PMTParamsDBWriter(**kwargs):
  mod = cms.EDAnalyzer('HFPhase1PMTParamsDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
