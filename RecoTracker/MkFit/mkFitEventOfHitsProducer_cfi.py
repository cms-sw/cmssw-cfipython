import FWCore.ParameterSet.Config as cms

mkFitEventOfHitsProducer = cms.EDProducer('MkFitEventOfHitsProducer',
  pixelHits = cms.InputTag('mkFitSiPixelHits'),
  stripHits = cms.InputTag('mkFitSiStripHits'),
  mightGet = cms.optional.untracked.vstring
)
