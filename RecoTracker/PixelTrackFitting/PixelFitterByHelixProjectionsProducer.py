import FWCore.ParameterSet.Config as cms

def PixelFitterByHelixProjectionsProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelFitterByHelixProjectionsProducer',
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
