import FWCore.ParameterSet.Config as cms

def SiStripBadStripDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
