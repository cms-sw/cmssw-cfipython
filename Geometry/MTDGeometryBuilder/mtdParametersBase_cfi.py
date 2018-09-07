import FWCore.ParameterSet.Config as cms

mtdParametersBase = cms.ESProducer('MTDParametersESModule',
  vitems = cms.VPSet(
  ),
  vpars = cms.vint32(),
  appendToDataLabel = cms.string('')
)
