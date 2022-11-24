import FWCore.ParameterSet.Config as cms

alignPCLThresholdsHGWriter = cms.EDAnalyzer('AlignPCLThresholdsHGWriter',
  minNRecords = cms.uint32(25000),
  record = cms.string('AlignPCLThresholdsHGRcd'),
  thresholds = cms.VPSet(
    cms.PSet()
  ),
  mightGet = cms.optional.untracked.vstring
)
