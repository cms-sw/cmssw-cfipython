import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBackPlaneCorrectionDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
