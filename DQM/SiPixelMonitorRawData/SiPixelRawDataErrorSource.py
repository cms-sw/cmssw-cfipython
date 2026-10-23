import FWCore.ParameterSet.Config as cms

def SiPixelRawDataErrorSource(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRawDataErrorSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
