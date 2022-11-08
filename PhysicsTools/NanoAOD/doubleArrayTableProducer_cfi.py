import FWCore.ParameterSet.Config as cms

doubleArrayTableProducer = cms.EDProducer('DoubleArrayTableProducer',
  name = cms.required.string,
  doc = cms.optional.string,
  src = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
