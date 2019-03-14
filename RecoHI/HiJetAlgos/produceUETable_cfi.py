import FWCore.ParameterSet.Config as cms

produceUETable = cms.EDAnalyzer('UETableProducer',
  txtFile = cms.string('example'),
  debug = cms.untracked.bool(False),
  jetCorrectorFormat = cms.untracked.bool(False)
)
