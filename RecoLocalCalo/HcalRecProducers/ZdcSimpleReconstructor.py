import FWCore.ParameterSet.Config as cms

def ZdcSimpleReconstructor(*args, **kwargs):
  mod = cms.EDProducer('ZdcSimpleReconstructor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
