import FWCore.ParameterSet.Config as cms

def SiPixelRawDataErrorSource(**kwargs):
  mod = cms.EDProducer('SiPixelRawDataErrorSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
