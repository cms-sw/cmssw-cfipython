import FWCore.ParameterSet.Config as cms

def HcalTBObjectUnpacker(**kwargs):
  mod = cms.EDProducer('HcalTBObjectUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
