import FWCore.ParameterSet.Config as cms

def AlignPCLThresholdsHGWriter(**kwargs):
  mod = cms.EDAnalyzer('AlignPCLThresholdsHGWriter',
    minNRecords = cms.uint32(25000),
    record = cms.string('AlignPCLThresholdsHGRcd'),
    thresholds = cms.VPSet(
      cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
