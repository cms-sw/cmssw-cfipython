import FWCore.ParameterSet.Config as cms

def L1TCaloStage2ParamsWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TCaloStage2ParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
