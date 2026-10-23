import FWCore.ParameterSet.Config as cms

def L1TCaloLayer1Validator(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TCaloLayer1Validator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
