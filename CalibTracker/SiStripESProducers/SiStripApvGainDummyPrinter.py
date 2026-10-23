import FWCore.ParameterSet.Config as cms

def SiStripApvGainDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
