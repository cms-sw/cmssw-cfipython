import FWCore.ParameterSet.Config as cms

def RPCAMCLinkMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCAMCLinkMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
