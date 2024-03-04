import FWCore.ParameterSet.Config as cms

def HcalCalibrator(**kwargs):
  mod = cms.EDAnalyzer('HcalCalibrator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
