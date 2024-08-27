import FWCore.ParameterSet.Config as cms

def JetResolutionScaleFactorDBReader(**kwargs):
  mod = cms.EDAnalyzer('JetResolutionScaleFactorDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
