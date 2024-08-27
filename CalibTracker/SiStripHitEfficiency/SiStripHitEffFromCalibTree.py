import FWCore.ParameterSet.Config as cms

def SiStripHitEffFromCalibTree(**kwargs):
  mod = cms.EDAnalyzer('SiStripHitEffFromCalibTree',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
