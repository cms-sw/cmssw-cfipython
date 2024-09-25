import FWCore.ParameterSet.Config as cms

def L1TCaloParamsUpdater(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TCaloParamsUpdater',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
