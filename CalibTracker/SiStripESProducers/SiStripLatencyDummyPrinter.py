import FWCore.ParameterSet.Config as cms

def SiStripLatencyDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripLatencyDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
