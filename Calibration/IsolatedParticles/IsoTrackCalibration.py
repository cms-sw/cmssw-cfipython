import FWCore.ParameterSet.Config as cms

def IsoTrackCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('IsoTrackCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
