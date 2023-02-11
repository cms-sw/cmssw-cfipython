import FWCore.ParameterSet.Config as cms

siPixelLorentzAnglePCLHarvesterMCS = cms.EDProducer('SiPixelLorentzAnglePCLHarvesterMCS',
  dqmDir = cms.string('AlCaReco/SiPixelLorentzAngle'),
  newmodulelist = cms.vstring(),
  fitRange = cms.vdouble(
    -1.5,
    1.5
  ),
  fitParameters = cms.vdouble(
    1,
    0.1,
    -1.6,
    0,
    1.6
  ),
  fitParametersMuHFit = cms.vdouble(
    0.08,
    0.08,
    0.08,
    0.08
  ),
  minHitsCut = cms.int32(1000),
  record = cms.string('SiPixelLorentzAngleRcdMCS'),
  mightGet = cms.optional.untracked.vstring
)
