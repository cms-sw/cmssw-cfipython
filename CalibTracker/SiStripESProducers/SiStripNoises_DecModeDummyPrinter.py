import FWCore.ParameterSet.Config as cms

def SiStripNoises_DecModeDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoises_DecModeDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
