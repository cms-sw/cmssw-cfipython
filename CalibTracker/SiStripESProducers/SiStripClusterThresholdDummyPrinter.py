import FWCore.ParameterSet.Config as cms

def SiStripClusterThresholdDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripClusterThresholdDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
