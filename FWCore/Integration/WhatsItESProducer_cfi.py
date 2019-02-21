import FWCore.ParameterSet.Config as cms

WhatsItESProducer = cms.ESProducer('WhatsItESProducer',
  test = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
