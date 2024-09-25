import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBackPlaneCorrectionDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
