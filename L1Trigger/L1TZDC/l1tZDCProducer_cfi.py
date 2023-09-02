import FWCore.ParameterSet.Config as cms

l1tZDCProducer = cms.EDProducer('L1TZDCProducer',
  zdcDigis = cms.InputTag('hcalDigis', 'ZDC'),
  bxFirst = cms.int32(-2),
  bxLast = cms.int32(2),
  sampleToCenterBX = cms.int32(4),
  mightGet = cms.optional.untracked.vstring
)
