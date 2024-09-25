import FWCore.ParameterSet.Config as cms

def PixelPopConCalibChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelPopConCalibChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
