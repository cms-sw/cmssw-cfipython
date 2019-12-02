import FWCore.ParameterSet.Config as cms

mkFitOutputConverter = cms.EDProducer('MkFitOutputConverter',
  hitsSeeds = cms.InputTag('mkFitInputConverter'),
  tracks = cms.InputTag('mkFitProducer'),
  seeds = cms.InputTag('initialStepSeeds'),
  measurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  propagatorAlong = cms.ESInputTag('', 'PropagatorWithMaterial'),
  propagatorOpposite = cms.ESInputTag('', 'PropagatorWithMaterialOpposite'),
  backwardFitInCMSSW = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
