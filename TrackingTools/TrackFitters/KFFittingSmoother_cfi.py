import FWCore.ParameterSet.Config as cms

KFFittingSmoother = cms.ESProducer('KFFittingSmootherESProducer',
  ComponentName = cms.string('KFFittingSmoother'),
  Fitter = cms.string('KFFitter'),
  Smoother = cms.string('KFSmoother'),
  EstimateCut = cms.double(-1),
  MaxFractionOutliers = cms.double(0.3),
  MaxNumberOfOutliers = cms.int32(3),
  MinDof = cms.int32(2),
  NoOutliersBeginEnd = cms.bool(False),
  MinNumberOfHits = cms.int32(5),
  RejectTracks = cms.bool(True),
  BreakTrajWith2ConsecutiveMissing = cms.bool(True),
  NoInvalidHitsBeginEnd = cms.bool(True),
  LogPixelProbabilityCut = cms.double(0),
  appendToDataLabel = cms.string('')
)
