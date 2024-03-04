import FWCore.ParameterSet.Config as cms

def ZdcSimpleReconstructor(**kwargs):
  mod = cms.EDProducer('ZdcSimpleReconstructor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
