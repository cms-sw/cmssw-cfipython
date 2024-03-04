import FWCore.ParameterSet.Config as cms

def L1TCaloParamsUpdater(**kwargs):
  mod = cms.EDAnalyzer('L1TCaloParamsUpdater',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
