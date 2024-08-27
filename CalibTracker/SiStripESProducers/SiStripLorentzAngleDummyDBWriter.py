import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
