import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
