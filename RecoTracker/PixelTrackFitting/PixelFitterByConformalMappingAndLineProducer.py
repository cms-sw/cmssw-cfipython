import FWCore.ParameterSet.Config as cms

def PixelFitterByConformalMappingAndLineProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelFitterByConformalMappingAndLineProducer',
    TTRHBuilder = cms.string('PixelTTRHBuilderWithoutAngle'),
    useFixImpactParameter = cms.bool(False),
    fixImpactParameter = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
