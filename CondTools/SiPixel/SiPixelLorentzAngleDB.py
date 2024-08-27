import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAngleDB(**kwargs):
  mod = cms.EDAnalyzer('SiPixelLorentzAngleDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
