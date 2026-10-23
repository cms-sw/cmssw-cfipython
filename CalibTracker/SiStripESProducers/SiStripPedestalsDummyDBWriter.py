import FWCore.ParameterSet.Config as cms

def SiStripPedestalsDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
