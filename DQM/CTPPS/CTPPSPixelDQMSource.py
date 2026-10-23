import FWCore.ParameterSet.Config as cms

def CTPPSPixelDQMSource(*args, **kwargs):
  mod = cms.EDProducer('CTPPSPixelDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
