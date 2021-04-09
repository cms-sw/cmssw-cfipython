import FWCore.ParameterSet.Config as cms

siPixelDigisClustersFromSoA = cms.EDProducer('SiPixelDigisClustersFromSoA',
  src = cms.InputTag('siPixelDigisSoA'),
  clusterThreshold_layer1 = cms.int32(2000),
  clusterThreshold_otherLayers = cms.int32(4000),
  mightGet = cms.optional.untracked.vstring
)
