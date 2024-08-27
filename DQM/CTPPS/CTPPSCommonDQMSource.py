import FWCore.ParameterSet.Config as cms

def CTPPSCommonDQMSource(**kwargs):
  mod = cms.EDProducer('CTPPSCommonDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
