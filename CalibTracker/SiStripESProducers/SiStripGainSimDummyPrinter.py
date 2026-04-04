import FWCore.ParameterSet.Config as cms

def SiStripGainSimDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainSimDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
