import FWCore.ParameterSet.Config as cms

def CTPPSTrackDistributionPlotter(**kwargs):
  mod = cms.EDAnalyzer('CTPPSTrackDistributionPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
