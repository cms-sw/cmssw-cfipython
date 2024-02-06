import FWCore.ParameterSet.Config as cms

mkFitSeedConverter = cms.EDProducer('MkFitSeedConverter',
  seeds = cms.InputTag('initialStepSeeds'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  maxNSeeds = cms.uint32(500000),
  mightGet = cms.optional.untracked.vstring
)
