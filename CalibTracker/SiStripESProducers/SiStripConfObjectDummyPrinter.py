import FWCore.ParameterSet.Config as cms

def SiStripConfObjectDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripConfObjectDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
