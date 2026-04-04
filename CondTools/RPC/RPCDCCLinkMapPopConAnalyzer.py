import FWCore.ParameterSet.Config as cms

def RPCDCCLinkMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCDCCLinkMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
