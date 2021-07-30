import FWCore.ParameterSet.Config as cms

mkFitEventOfHitsProducer = cms.EDProducer('MkFitEventOfHitsProducer',
  pixelHits = cms.InputTag('mkFitSiPixelHits'),
  stripHits = cms.InputTag('mkFitSiStripHits'),
  useStripStripQualityDB = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
