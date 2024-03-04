import FWCore.ParameterSet.Config as cms

def LHCInfoPerLSWriter(**kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerLSWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
