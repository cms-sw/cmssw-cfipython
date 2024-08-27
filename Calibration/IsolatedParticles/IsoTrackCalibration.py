import FWCore.ParameterSet.Config as cms

def IsoTrackCalibration(**kwargs):
  mod = cms.EDAnalyzer('IsoTrackCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
