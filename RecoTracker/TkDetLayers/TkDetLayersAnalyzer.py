import FWCore.ParameterSet.Config as cms

def TkDetLayersAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TkDetLayersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
