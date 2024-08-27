import FWCore.ParameterSet.Config as cms

def PixelFitterByConformalMappingAndLineProducer(**kwargs):
  mod = cms.EDProducer('PixelFitterByConformalMappingAndLineProducer',
    TTRHBuilder = cms.string('PixelTTRHBuilderWithoutAngle'),
    useFixImpactParameter = cms.bool(False),
    fixImpactParameter = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
