import FWCore.ParameterSet.Config as cms

def SiStripCalibLorentzAngle(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCalibLorentzAngle',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
