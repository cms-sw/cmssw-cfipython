import FWCore.ParameterSet.Config as cms

def SiStripBaseDelayDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBaseDelayDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
