import FWCore.ParameterSet.Config as cms

def PixelPopConDisabledModAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PixelPopConDisabledModAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
