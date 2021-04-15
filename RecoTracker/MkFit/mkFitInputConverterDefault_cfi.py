import FWCore.ParameterSet.Config as cms

mkFitInputConverterDefault = cms.EDProducer('MkFitInputConverter',
  pixelRecHits = cms.InputTag('siPixelRecHits'),
  stripRphiRecHits = cms.InputTag('siStripMatchedRecHits', 'rphiRecHit'),
  stripStereoRecHits = cms.InputTag('siStripMatchedRecHits', 'stereoRecHit'),
  seeds = cms.InputTag('initialStepSeeds'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  minGoodStripCharge = cms.PSet(
    value = cms.required.double
  ),
  mightGet = cms.optional.untracked.vstring
)
