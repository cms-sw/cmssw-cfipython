import FWCore.ParameterSet.Config as cms

def SiStripBaseDelayDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBaseDelayDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
