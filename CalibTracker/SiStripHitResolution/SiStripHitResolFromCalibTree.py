import FWCore.ParameterSet.Config as cms

def SiStripHitResolFromCalibTree(**kwargs):
  mod = cms.EDAnalyzer('SiStripHitResolFromCalibTree',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
