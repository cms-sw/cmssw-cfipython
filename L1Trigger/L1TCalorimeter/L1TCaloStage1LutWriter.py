import FWCore.ParameterSet.Config as cms

def L1TCaloStage1LutWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TCaloStage1LutWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
