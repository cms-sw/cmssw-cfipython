import FWCore.ParameterSet.Config as cms

def KFFittingSmootherESProducer(*args, **kwargs):
  mod = cms.ESProducer('KFFittingSmootherESProducer',
    ComponentName = cms.string('KFFittingSmoother'),
    Fitter = cms.string('KFFitter'),
    Smoother = cms.string('KFSmoother'),
    EstimateCut = cms.double(-1),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    NoOutliersBeginEnd = cms.bool(False),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    HighEtaSwitch = cms.double(5),
    RejectTracks = cms.bool(True),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    NoInvalidHitsBeginEnd = cms.bool(True),
    LogPixelProbabilityCut = cms.double(0),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
