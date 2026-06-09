import FWCore.ParameterSet.Config as cms

def SiStripNoisesDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
