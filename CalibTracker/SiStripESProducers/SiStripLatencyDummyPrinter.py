import FWCore.ParameterSet.Config as cms

def SiStripLatencyDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripLatencyDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
