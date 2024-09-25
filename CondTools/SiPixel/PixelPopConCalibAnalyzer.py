import FWCore.ParameterSet.Config as cms

def PixelPopConCalibAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelPopConCalibAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
