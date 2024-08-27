import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAngleDBLoader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelLorentzAngleDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
