import FWCore.ParameterSet.Config as cms

def SiPixelTrackResidualSource(**kwargs):
  mod = cms.EDProducer('SiPixelTrackResidualSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
