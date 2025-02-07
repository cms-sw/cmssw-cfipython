import FWCore.ParameterSet.Config as cms

def L1TZDCProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TZDCProducer',
    hcalTPDigis = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
