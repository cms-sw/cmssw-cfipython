import FWCore.ParameterSet.Config as cms

def DTHVStatusPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTHVStatusPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
