import FWCore.ParameterSet.Config as cms

def CalibrationTrackSelectorFromDetIdList(*args, **kwargs):
  mod = cms.EDProducer('CalibrationTrackSelectorFromDetIdList',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
