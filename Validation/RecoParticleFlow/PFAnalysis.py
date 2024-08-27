import FWCore.ParameterSet.Config as cms

def PFAnalysis(**kwargs):
  mod = cms.EDAnalyzer('PFAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
