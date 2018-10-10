import FWCore.ParameterSet.Config as cms

BJetEnergyRegressionMVA = cms.EDProducer('BJetEnergyRegressionMVA',
  variables = cms.PSet(),
  backend = cms.string('TMVA'),
  inputTensorName = cms.string(''),
  outputTensorName = cms.string(''),
  outputNames = cms.vstring(),
  outputFormulas = cms.vstring(),
  nThreads = cms.uint32(1),
  singleThreadPool = cms.string('no_threads')
)
