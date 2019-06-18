import FWCore.ParameterSet.Config as cms

WhatsItESProducer = cms.ESProducer('WhatsItESProducer',
  doodadLabel = cms.optional.string,
  test = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
