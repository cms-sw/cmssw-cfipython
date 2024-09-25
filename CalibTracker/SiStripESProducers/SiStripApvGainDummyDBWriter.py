import FWCore.ParameterSet.Config as cms

def SiStripApvGainDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
