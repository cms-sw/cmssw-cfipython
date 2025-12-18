import FWCore.ParameterSet.Config as cms

def OutsideInMuonSeeder(*args, **kwargs):
  mod = cms.EDProducer('OutsideInMuonSeeder',
    src = cms.InputTag('muons'),
    cut = cms.string(''),
    layersToTry = cms.int32(3),
    hitsToTry = cms.int32(3),
    fromVertex = cms.bool(True),
    errorRescaleFactor = cms.double(2),
    trackerPropagator = cms.string(''),
    muonPropagator = cms.string(''),
    measurementTkEvent = cms.InputTag('MeasurementTrackerEvent'),
    hitCollector = cms.string(''),
    updatorLabel = cms.string('KFUpdator'),
    minEtaForTEC = cms.double(0.7),
    maxEtaForTOB = cms.double(1.8),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
