import FWCore.ParameterSet.Config as cms

def SiStripBaseDelayDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBaseDelayDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
