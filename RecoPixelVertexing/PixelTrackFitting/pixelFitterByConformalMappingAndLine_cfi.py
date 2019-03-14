import FWCore.ParameterSet.Config as cms

pixelFitterByConformalMappingAndLine = cms.EDProducer('PixelFitterByConformalMappingAndLineProducer',
  TTRHBuilder = cms.string('PixelTTRHBuilderWithoutAngle'),
  useFixImpactParameter = cms.bool(False),
  fixImpactParameter = cms.double(0)
)
