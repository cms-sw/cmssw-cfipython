import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDepDummyPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBackPlaneCorrectionDepDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
