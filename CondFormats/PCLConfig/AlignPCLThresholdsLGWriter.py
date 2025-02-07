import FWCore.ParameterSet.Config as cms

def AlignPCLThresholdsLGWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('AlignPCLThresholdsLGWriter',
    minNRecords = cms.uint32(25000),
    record = cms.string('AlignPCLThresholdsRcd'),
    thresholds = cms.VPSet(
      cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
