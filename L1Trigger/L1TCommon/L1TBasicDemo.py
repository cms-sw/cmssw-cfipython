import FWCore.ParameterSet.Config as cms

def L1TBasicDemo(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TBasicDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
