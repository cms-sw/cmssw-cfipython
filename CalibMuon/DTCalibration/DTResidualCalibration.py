import FWCore.ParameterSet.Config as cms

def DTResidualCalibration(**kwargs):
  mod = cms.EDAnalyzer('DTResidualCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
