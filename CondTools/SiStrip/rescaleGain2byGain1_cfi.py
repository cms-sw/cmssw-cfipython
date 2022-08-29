import FWCore.ParameterSet.Config as cms

rescaleGain2byGain1 = cms.EDAnalyzer('SiStripApvGainRescaler',
  Record = cms.string('SiStripApvGainRcd'),
  printDebug = cms.untracked.uint32(1),
  mightGet = cms.optional.untracked.vstring
)
