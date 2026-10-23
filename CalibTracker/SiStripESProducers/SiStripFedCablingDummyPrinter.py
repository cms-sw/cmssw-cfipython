import FWCore.ParameterSet.Config as cms

def SiStripFedCablingDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
