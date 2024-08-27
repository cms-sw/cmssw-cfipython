import FWCore.ParameterSet.Config as cms

def SiStripCalibLorentzAngle(**kwargs):
  mod = cms.EDAnalyzer('SiStripCalibLorentzAngle',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
