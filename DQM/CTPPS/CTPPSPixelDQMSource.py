import FWCore.ParameterSet.Config as cms

def CTPPSPixelDQMSource(**kwargs):
  mod = cms.EDProducer('CTPPSPixelDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
