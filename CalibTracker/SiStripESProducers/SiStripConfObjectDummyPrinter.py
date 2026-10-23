import FWCore.ParameterSet.Config as cms

def SiStripConfObjectDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripConfObjectDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
