import FWCore.ParameterSet.Config as cms

def DTUserKeyedConfigPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTUserKeyedConfigPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
