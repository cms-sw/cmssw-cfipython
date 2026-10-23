import FWCore.ParameterSet.Config as cms

def DTLVStatusPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTLVStatusPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
