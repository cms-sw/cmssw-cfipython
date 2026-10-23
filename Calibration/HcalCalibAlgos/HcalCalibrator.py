import FWCore.ParameterSet.Config as cms

def HcalCalibrator(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalCalibrator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
