import FWCore.ParameterSet.Config as cms

ctppsModifiedOpticalFunctionsESSource = cms.ESProducer('CTPPSModifiedOpticalFunctionsESSource',
  inputOpticsLabel = cms.string(''),
  outputOpticsLabel = cms.string('modified'),
  scenario = cms.string('none'),
  factor = cms.double(0),
  rpId_45_N = cms.uint32(0),
  rpId_45_F = cms.uint32(0),
  rpId_56_N = cms.uint32(0),
  rpId_56_F = cms.uint32(0),
  appendToDataLabel = cms.string('')
)
