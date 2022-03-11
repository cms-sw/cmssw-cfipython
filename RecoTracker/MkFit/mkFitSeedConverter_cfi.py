import FWCore.ParameterSet.Config as cms

mkFitSeedConverter = cms.EDProducer('MkFitSeedConverter',
  seeds = cms.InputTag('initialStepSeeds'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  mightGet = cms.optional.untracked.vstring
)
