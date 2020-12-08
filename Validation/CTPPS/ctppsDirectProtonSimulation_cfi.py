import FWCore.ParameterSet.Config as cms

ctppsDirectProtonSimulation = cms.EDProducer('CTPPSDirectProtonSimulation',
  verbosity = cms.untracked.uint32(0),
  lhcInfoLabel = cms.string(''),
  opticsLabel = cms.string(''),
  hepMCTag = cms.InputTag('generator', 'unsmeared'),
  produceScoringPlaneHits = cms.bool(True),
  produceRecHits = cms.bool(True),
  useEmpiricalApertures = cms.bool(True),
  useTimingRPEfficiency = cms.bool(False),
  produceHitsRelativeToBeam = cms.bool(True),
  roundToPitch = cms.bool(True),
  checkIsHit = cms.bool(True),
  pitchStrips = cms.double(0.066),
  insensitiveMarginStrips = cms.double(0.034),
  pitchPixelsHor = cms.double(0.1),
  pitchPixelsVer = cms.double(0.15),
  mightGet = cms.optional.untracked.vstring
)
