import FWCore.ParameterSet.Config as cms

edmtestAlignPCLThresholdsReaderAlignPCLThresholdsAlignPCLThresholdsRcd = cms.EDAnalyzer('AlignPCLThresholdsLGReader',
  printDebug = cms.untracked.bool(True),
  outputFile = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
