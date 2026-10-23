import FWCore.ParameterSet.Config as cms

def PixelPopConDisabledModAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelPopConDisabledModAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
