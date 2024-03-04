import FWCore.ParameterSet.Config as cms

def MuDTSegmentExtTableProducer(**kwargs):
  mod = cms.EDProducer('MuDTSegmentExtTableProducer',
    name = cms.string('dtSegment'),
    src = cms.InputTag('dt4DSegments'),
    fillExtrapolation = cms.bool(True),
    fillHits = cms.bool(True),
    tTrigMode = cms.string('DTTTrigSyncFromDB'),
    tTrigModeConfig = cms.PSet(
      doTOFCorrection = cms.bool(True),
      tofCorrType = cms.int32(2),
      vPropWire = cms.double(24.4),
      doWirePropCorrection = cms.bool(True),
      wirePropCorrType = cms.int32(0),
      tTrigLabel = cms.string(''),
      doT0Correction = cms.bool(True),
      t0Label = cms.string(''),
      debug = cms.untracked.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
