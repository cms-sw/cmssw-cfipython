import FWCore.ParameterSet.Config as cms

def MPISender(*args, **kwargs):
  mod = cms.EDProducer('MPISender',
    upstream = cms.InputTag('source'),
    products = cms.vstring(),
    instance = cms.int32(0),
    activity = cms.InputTag(''),
    enableTrivialSerialisation = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
