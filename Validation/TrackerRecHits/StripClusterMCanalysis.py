import FWCore.ParameterSet.Config as cms

def StripClusterMCanalysis(**kwargs):
  mod = cms.EDAnalyzer('StripClusterMCanalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
