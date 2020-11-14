import FWCore.ParameterSet.Config as cms

siPixelStatusProducer = cms.EDProducer('SiPixelStatusProducer',
  SiPixelStatusProducerParameters = cms.PSet(
    pixelClusterLabel = cms.untracked.InputTag('siPixelClusters', '', 'RECO'),
    badPixelFEDChannelCollections = cms.VInputTag('siPixelDigis')
  ),
  mightGet = cms.optional.untracked.vstring
)
