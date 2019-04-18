import FWCore.ParameterSet.Config as cms

ftsPileupFromScalers = cms.EDAnalyzer('FTSLuminosityFromScalers',
  source = cms.InputTag('scalersRawToDigi'),
  type = cms.string('Pileup'),
  name = cms.string('pileup'),
  title = cms.string('pileup'),
  label = cms.string('pileup'),
  range = cms.double(40),
  resolution = cms.double(1)
)
