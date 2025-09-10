import FWCore.ParameterSet.Config as cms

def SiPixelTrackResidualSource(*args, **kwargs):
  mod = cms.EDProducer('SiPixelTrackResidualSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
