import FWCore.ParameterSet.Config as cms

def PixelFitterByHelixProjectionsProducer(**kwargs):
  mod = cms.EDProducer('PixelFitterByHelixProjectionsProducer',
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
