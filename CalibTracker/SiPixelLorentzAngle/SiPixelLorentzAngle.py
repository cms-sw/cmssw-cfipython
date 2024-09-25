import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAngle(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelLorentzAngle',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
