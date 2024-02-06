import FWCore.ParameterSet.Config as cms

edmtestAlignPCLThresholdsReaderAlignPCLThresholdsHGAlignPCLThresholdsHGRcd = cms.EDAnalyzer('AlignPCLThresholdsHGReader',
  printDebug = cms.untracked.bool(True),
  outputFile = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
