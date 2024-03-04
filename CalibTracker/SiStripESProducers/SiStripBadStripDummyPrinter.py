import FWCore.ParameterSet.Config as cms

def SiStripBadStripDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
