import FWCore.ParameterSet.Config as cms

siPixelPhase2DigiToClusterCUDA = cms.EDProducer('SiPixelPhase2DigiToClusterCUDA',
  IncludeErrors = cms.bool(True),
  clusterThreshold_layer1 = cms.int32(4000),
  clusterThreshold_otherLayers = cms.int32(4000),
  InputDigis = cms.InputTag('simSiPixelDigis', 'Pixel'),
  mightGet = cms.optional.untracked.vstring
)
