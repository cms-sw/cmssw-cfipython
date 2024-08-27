import FWCore.ParameterSet.Config as cms

def SiStripNoises_PeakModeDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripNoises_PeakModeDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
