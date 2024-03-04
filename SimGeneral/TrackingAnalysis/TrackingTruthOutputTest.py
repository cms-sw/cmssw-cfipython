import FWCore.ParameterSet.Config as cms

def TrackingTruthOutputTest(**kwargs):
  mod = cms.EDAnalyzer('TrackingTruthOutputTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
