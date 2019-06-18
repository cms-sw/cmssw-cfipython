import FWCore.ParameterSet.Config as cms

siPixelStatusProducer = cms.EDProducer('SiPixelStatusProducer',
  SiPixelStatusProducerParameters = cms.PSet(
    resetEveryNLumi = cms.untracked.int32(1),
    pixelClusterLabel = cms.untracked.InputTag('siPixelClusters', '', 'RECO'),
    badPixelFEDChannelCollections = cms.VInputTag('siPixelDigis')
  ),
  mightGet = cms.optional.untracked.vstring
)
