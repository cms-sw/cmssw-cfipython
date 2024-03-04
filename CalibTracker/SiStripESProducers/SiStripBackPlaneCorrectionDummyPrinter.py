import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBackPlaneCorrectionDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
