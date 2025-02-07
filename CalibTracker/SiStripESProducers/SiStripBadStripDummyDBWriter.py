import FWCore.ParameterSet.Config as cms

def SiStripBadStripDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
