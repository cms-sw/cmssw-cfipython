import FWCore.ParameterSet.Config as cms

def TrackChargeSelector(*args, **kwargs):
  mod = cms.EDFilter('TrackChargeSelector',
    src = cms.InputTag(''),
    charge = cms.int32(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
