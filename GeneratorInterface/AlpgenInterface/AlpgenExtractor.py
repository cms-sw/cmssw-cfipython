import FWCore.ParameterSet.Config as cms

def AlpgenExtractor(*args, **kwargs):
  mod = cms.EDAnalyzer('AlpgenExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
