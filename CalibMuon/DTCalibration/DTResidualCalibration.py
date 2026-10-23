import FWCore.ParameterSet.Config as cms

def DTResidualCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('DTResidualCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
