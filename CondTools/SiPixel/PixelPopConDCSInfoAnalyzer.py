import FWCore.ParameterSet.Config as cms

def PixelPopConDCSInfoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelPopConDCSInfoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
