import FWCore.ParameterSet.Config as cms

def SiStripBadChannelDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadChannelDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
