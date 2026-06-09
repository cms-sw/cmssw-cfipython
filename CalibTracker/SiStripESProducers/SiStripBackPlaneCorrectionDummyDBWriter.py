import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBackPlaneCorrectionDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
