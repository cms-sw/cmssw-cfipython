import FWCore.ParameterSet.Config as cms

def SiStripDetVOffDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
