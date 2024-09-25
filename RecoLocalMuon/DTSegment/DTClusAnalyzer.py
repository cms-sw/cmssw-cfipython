import FWCore.ParameterSet.Config as cms

def DTClusAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTClusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
