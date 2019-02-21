import FWCore.ParameterSet.Config as cms

pixelTrackFilterByKinematics = cms.EDProducer('PixelTrackFilterByKinematicsProducer',
  ptMin = cms.double(0.1),
  nSigmaInvPtTolerance = cms.double(0),
  tipMax = cms.double(1),
  nSigmaTipMaxTolerance = cms.double(0),
  chi2 = cms.double(1000)
)
