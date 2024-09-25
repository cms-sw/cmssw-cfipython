import FWCore.ParameterSet.Config as cms

def SiStripBadModuleDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadModuleDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
