import FWCore.ParameterSet.Config as cms

def SiStripGainFromCalibTree(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainFromCalibTree',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
