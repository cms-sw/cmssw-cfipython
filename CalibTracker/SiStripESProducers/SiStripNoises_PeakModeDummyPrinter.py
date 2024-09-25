import FWCore.ParameterSet.Config as cms

def SiStripNoises_PeakModeDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoises_PeakModeDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
