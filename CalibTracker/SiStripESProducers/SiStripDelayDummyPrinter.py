import FWCore.ParameterSet.Config as cms

def SiStripDelayDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDelayDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
