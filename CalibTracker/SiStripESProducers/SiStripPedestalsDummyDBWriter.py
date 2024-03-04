import FWCore.ParameterSet.Config as cms

def SiStripPedestalsDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
