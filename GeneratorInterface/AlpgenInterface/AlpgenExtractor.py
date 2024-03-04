import FWCore.ParameterSet.Config as cms

def AlpgenExtractor(**kwargs):
  mod = cms.EDAnalyzer('AlpgenExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
