import FWCore.ParameterSet.Config as cms

def JetResolutionDBWriter(**kwargs):
  mod = cms.EDAnalyzer('JetResolutionDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
