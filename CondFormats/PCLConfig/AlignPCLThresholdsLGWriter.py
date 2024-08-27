import FWCore.ParameterSet.Config as cms

def AlignPCLThresholdsLGWriter(**kwargs):
  mod = cms.EDAnalyzer('AlignPCLThresholdsLGWriter',
    minNRecords = cms.uint32(25000),
    record = cms.string('AlignPCLThresholdsRcd'),
    thresholds = cms.VPSet(
      cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
