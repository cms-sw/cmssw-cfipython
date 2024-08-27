import FWCore.ParameterSet.Config as cms

def SiStripGainFromCalibTree(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainFromCalibTree',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
