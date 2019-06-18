import FWCore.ParameterSet.Config as cms

rescaleGain2byGain1 = cms.EDAnalyzer('SiStripApvGainRescaler',
  Record = cms.string('SiStripApvGainRcd'),
  mightGet = cms.optional.untracked.vstring
)
