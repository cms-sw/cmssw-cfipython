import FWCore.ParameterSet.Config as cms

alignPCLThresholdsLGWriter = cms.EDAnalyzer('AlignPCLThresholdsLGWriter',
  minNRecords = cms.uint32(25000),
  record = cms.string('AlignPCLThresholdsRcd'),
  thresholds = cms.VPSet(
    cms.PSet()
  ),
  mightGet = cms.optional.untracked.vstring
)
