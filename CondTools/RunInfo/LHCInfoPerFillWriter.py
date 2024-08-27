import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillWriter(**kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
