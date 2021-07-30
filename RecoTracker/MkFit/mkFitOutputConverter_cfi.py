import FWCore.ParameterSet.Config as cms

mkFitOutputConverter = cms.EDProducer('MkFitOutputConverter',
  mkFitEventOfHits = cms.InputTag('mkFitEventOfHits'),
  mkFitPixelHits = cms.InputTag('mkFitSiPixelHits'),
  mkFitStripHits = cms.InputTag('mkFitSiStripHits'),
  mkFitSeeds = cms.InputTag('mkFitSeedConverter'),
  tracks = cms.InputTag('mkFitProducer'),
  seeds = cms.InputTag('initialStepSeeds'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  propagatorAlong = cms.ESInputTag('', 'PropagatorWithMaterial'),
  propagatorOpposite = cms.ESInputTag('', 'PropagatorWithMaterialOpposite'),
  mightGet = cms.optional.untracked.vstring
)
