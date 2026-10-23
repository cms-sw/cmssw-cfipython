import FWCore.ParameterSet.Config as cms

def RPCAMCLinkMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCAMCLinkMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
