import FWCore.ParameterSet.Config as cms

def SiStripNoises_DecModeDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripNoises_DecModeDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
