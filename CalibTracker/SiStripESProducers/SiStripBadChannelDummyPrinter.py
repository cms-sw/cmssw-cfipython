import FWCore.ParameterSet.Config as cms

def SiStripBadChannelDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadChannelDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
