import FWCore.ParameterSet.Config as cms

def L1TCaloStage2ParamsWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TCaloStage2ParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
