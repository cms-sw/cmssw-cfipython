import FWCore.ParameterSet.Config as cms

l1tZDCProducer = cms.EDProducer('L1TZDCProducer',
  hcalTPDigis = cms.InputTag('simHcalTriggerPrimitiveDigis'),
  bxFirst = cms.int32(-2),
  bxLast = cms.int32(2),
  mightGet = cms.optional.untracked.vstring
)
