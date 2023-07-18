import FWCore.ParameterSet.Config as cms

EvFFEDSelector = cms.EDProducer('EvFFEDSelector',
  inputTag = cms.InputTag('source'),
  fedList = cms.vuint32(
    812,
    1023
  ),
  mightGet = cms.optional.untracked.vstring
)
