import FWCore.ParameterSet.Config as cms

def SiStripConfObjectDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripConfObjectDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
