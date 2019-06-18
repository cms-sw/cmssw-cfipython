import FWCore.ParameterSet.Config as cms

PhoVIDNestedWPBitmapProducer = cms.EDProducer('PhoVIDNestedWPBitmapProducer',
  src = cms.required.InputTag,
  WorkingPoints = cms.required.vstring,
  mightGet = cms.optional.untracked.vstring
)
