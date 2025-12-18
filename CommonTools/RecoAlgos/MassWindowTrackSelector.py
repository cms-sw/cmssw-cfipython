import FWCore.ParameterSet.Config as cms

def MassWindowTrackSelector(*args, **kwargs):
  mod = cms.EDFilter('MassWindowTrackSelector',
    src = cms.InputTag(''),
    rangeMin = cms.double(0),
    rangeMax = cms.double(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
