import FWCore.ParameterSet.Config as cms

def CastorRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('CastorRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
