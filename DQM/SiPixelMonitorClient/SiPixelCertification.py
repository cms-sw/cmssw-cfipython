import FWCore.ParameterSet.Config as cms

def SiPixelCertification(*args, **kwargs):
  mod = cms.EDProducer('SiPixelCertification',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
