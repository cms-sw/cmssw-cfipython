import FWCore.ParameterSet.Config as cms

def MeasurementTrackerTest(**kwargs):
  mod = cms.EDAnalyzer('MeasurementTrackerTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
