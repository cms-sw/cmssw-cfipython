import FWCore.ParameterSet.Config as cms

dqmScaleToClient = cms.EDAnalyzer('DQMScaleToClient',
  outputme = cms.PSet(
    folder = cms.string(''),
    name = cms.string(''),
    factor = cms.double(1)
  ),
  inputme = cms.PSet(
    folder = cms.string(''),
    name = cms.string('')
  )
)
