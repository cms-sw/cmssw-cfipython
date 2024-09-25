import FWCore.ParameterSet.Config as cms

def GctErrorAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GctErrorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
