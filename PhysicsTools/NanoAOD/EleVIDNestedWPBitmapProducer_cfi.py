import FWCore.ParameterSet.Config as cms

EleVIDNestedWPBitmapProducer = cms.EDProducer('EleVIDNestedWPBitmapProducer',
  src = cms.required.InputTag,
  WorkingPoints = cms.required.vstring,
  mightGet = cms.optional.untracked.vstring
)
