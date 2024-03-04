import FWCore.ParameterSet.Config as cms

def TkDetLayersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TkDetLayersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
