import FWCore.ParameterSet.Config as cms

def CTPPSTrackDistributionPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSTrackDistributionPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
