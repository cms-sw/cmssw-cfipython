import FWCore.ParameterSet.Config as cms

def SiStripThresholdDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripThresholdDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
