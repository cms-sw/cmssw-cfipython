import FWCore.ParameterSet.Config as cms

def SiStripPedestalsDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
