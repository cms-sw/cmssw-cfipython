import FWCore.ParameterSet.Config as cms

def SiStripBadModuleDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadModuleDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
