import FWCore.ParameterSet.Config as cms

alignPCLThresholdsWriter = cms.EDAnalyzer('AlignPCLThresholdsWriter',
  record = cms.string('AlignPCLThresholdsRcd'),
  minNRecords = cms.uint32(25000),
  thresholds = cms.VPSet(
    cms.PSet()
  ),
  mightGet = cms.optional.untracked.vstring
)
