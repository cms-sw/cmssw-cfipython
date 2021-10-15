import FWCore.ParameterSet.Config as cms

siPixelLorentzAnglePCLHarvester = cms.EDProducer('SiPixelLorentzAnglePCLHarvester',
  newmodulelist = cms.vstring(),
  dqmDir = cms.string('AlCaReco/SiPixelLorentzAngle'),
  fitProbCut = cms.double(0.5),
  record = cms.string('SiPixelLorentzAngleRcd'),
  mightGet = cms.optional.untracked.vstring
)
