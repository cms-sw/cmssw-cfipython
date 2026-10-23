import FWCore.ParameterSet.Config as cms

def RPCLBLinkMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCLBLinkMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
