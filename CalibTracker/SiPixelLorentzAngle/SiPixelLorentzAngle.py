import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAngle(**kwargs):
  mod = cms.EDAnalyzer('SiPixelLorentzAngle',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
