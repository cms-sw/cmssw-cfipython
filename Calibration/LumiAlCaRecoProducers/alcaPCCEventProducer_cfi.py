import FWCore.ParameterSet.Config as cms

alcaPCCEventProducer = cms.EDProducer('AlcaPCCEventProducer',
  pixelClusterLabel = cms.InputTag('siPixelClustersForLumi'),
  trigstring = cms.untracked.string('alcaPCCEvent'),
  mightGet = cms.optional.untracked.vstring
)
