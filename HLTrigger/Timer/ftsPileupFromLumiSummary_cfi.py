import FWCore.ParameterSet.Config as cms

ftsPileupFromLumiSummary = cms.EDAnalyzer('FTSLuminosityFromLumiSummary',
  source = cms.InputTag('lumiProducer'),
  crossSection = cms.double(69.3),
  type = cms.string('Pileup'),
  name = cms.string('pileup'),
  title = cms.string('pileup'),
  label = cms.string('pileup'),
  range = cms.double(40),
  resolution = cms.double(1)
)
