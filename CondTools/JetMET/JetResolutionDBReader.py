import FWCore.ParameterSet.Config as cms

def JetResolutionDBReader(**kwargs):
  mod = cms.EDAnalyzer('JetResolutionDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
