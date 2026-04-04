import FWCore.ParameterSet.Config as cms

def SiStripHitResolFromCalibTree(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripHitResolFromCalibTree',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
