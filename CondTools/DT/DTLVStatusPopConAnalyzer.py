import FWCore.ParameterSet.Config as cms

def DTLVStatusPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTLVStatusPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
