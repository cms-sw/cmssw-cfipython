import FWCore.ParameterSet.Config as cms

def SiStripBadModuleDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadModuleDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
