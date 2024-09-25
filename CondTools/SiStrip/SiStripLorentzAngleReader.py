import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
