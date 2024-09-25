import FWCore.ParameterSet.Config as cms

def DTKeyedConfigPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTKeyedConfigPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
