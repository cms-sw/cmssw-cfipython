import FWCore.ParameterSet.Config as cms

l1TStage2RatioClient = cms.EDProducer('L1TStage2RatioClient',
  monitorDir = cms.untracked.string(''),
  inputNum = cms.untracked.string(''),
  inputDen = cms.untracked.string(''),
  ratioName = cms.untracked.string('ratio'),
  ratioTitle = cms.untracked.string('ratio'),
  yAxisTitle = cms.untracked.string(''),
  binomialErr = cms.untracked.bool(True),
  ignoreBin = cms.untracked.vint32()
)
