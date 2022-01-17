import FWCore.ParameterSet.Config as cms

siPixelLorentzAnglePCLHarvester = cms.EDProducer('SiPixelLorentzAnglePCLHarvester',
  newmodulelist = cms.vstring(),
  dqmDir = cms.string('AlCaReco/SiPixelLorentzAngle'),
  fitChi2Cut = cms.double(20),
  minHitsCut = cms.int32(10000),
  record = cms.string('SiPixelLorentzAngleRcd'),
  mightGet = cms.optional.untracked.vstring
)
