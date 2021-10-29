import FWCore.ParameterSet.Config as cms

_MeasurementTrackerESProducer_default = cms.ESProducer('MeasurementTrackerESProducer',
  ComponentName = cms.string(''),
  PixelCPE = cms.string('PixelCPEGeneric'),
  StripCPE = cms.string('StripCPEfromTrackAngle'),
  HitMatcher = cms.string('StandardMatcher'),
  Phase2StripCPE = cms.string(''),
  SiStripQualityLabel = cms.string(''),
  UseStripModuleQualityDB = cms.bool(True),
  DebugStripModuleQualityDB = cms.untracked.bool(False),
  UseStripAPVFiberQualityDB = cms.bool(True),
  DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
  MaskBadAPVFibers = cms.bool(True),
  UseStripStripQualityDB = cms.bool(True),
  DebugStripStripQualityDB = cms.untracked.bool(False),
  badStripCuts = cms.PSet(
    TIB = cms.PSet(
      maxBad = cms.uint32(4),
      maxConsecutiveBad = cms.uint32(2)
    ),
    TOB = cms.PSet(
      maxBad = cms.uint32(4),
      maxConsecutiveBad = cms.uint32(2)
    ),
    TID = cms.PSet(
      maxBad = cms.uint32(4),
      maxConsecutiveBad = cms.uint32(2)
    ),
    TEC = cms.PSet(
      maxBad = cms.uint32(4),
      maxConsecutiveBad = cms.uint32(2)
    )
  ),
  UsePixelModuleQualityDB = cms.bool(True),
  DebugPixelModuleQualityDB = cms.untracked.bool(False),
  UsePixelROCQualityDB = cms.bool(True),
  DebugPixelROCQualityDB = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
