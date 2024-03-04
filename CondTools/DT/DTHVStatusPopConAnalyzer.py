import FWCore.ParameterSet.Config as cms

def DTHVStatusPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTHVStatusPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
