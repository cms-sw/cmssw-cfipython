import FWCore.ParameterSet.Config as cms

AlignPCLThresholdsReader = cms.EDAnalyzer('AlignPCLThresholdsReader',
  printDebug = cms.untracked.bool(True),
  outputFile = cms.untracked.string('')
)
