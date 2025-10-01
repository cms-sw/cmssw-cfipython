import FWCore.ParameterSet.Config as cms

def L1TZDCEtSumsProducer(**kwargs):
  mod = cms.EDProducer('L1TZDCEtSumsProducer',
    hcalTPDigis = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
