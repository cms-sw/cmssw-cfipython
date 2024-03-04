import FWCore.ParameterSet.Config as cms

def SiStripFedCablingDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
