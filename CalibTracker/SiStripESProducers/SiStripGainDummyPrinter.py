import FWCore.ParameterSet.Config as cms

def SiStripGainDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
