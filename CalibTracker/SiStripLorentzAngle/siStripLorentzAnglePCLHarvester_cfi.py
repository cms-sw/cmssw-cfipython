import FWCore.ParameterSet.Config as cms

siStripLorentzAnglePCLHarvester = cms.EDProducer('SiStripLorentzAnglePCLHarvester',
  debugMode = cms.bool(False),
  dqmDir = cms.string('AlCaReco/SiStripLorentzAngle'),
  fitRange = cms.vdouble(
    0,
    0
  ),
  record = cms.string('SiStripLorentzAngleRcd'),
  mightGet = cms.optional.untracked.vstring
)
