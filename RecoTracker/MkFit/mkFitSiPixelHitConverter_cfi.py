import FWCore.ParameterSet.Config as cms

mkFitSiPixelHitConverter = cms.EDProducer('MkFitSiPixelHitConverter',
  hits = cms.InputTag('siPixelRecHits'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  mightGet = cms.optional.untracked.vstring
)
