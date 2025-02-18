import FWCore.ParameterSet.Config as cms

def AlignPCLThresholdsHGWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('AlignPCLThresholdsHGWriter',
    minNRecords = cms.uint32(25000),
    record = cms.string('AlignPCLThresholdsHGRcd'),
    thresholds = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        alignableId = cms.required.string,
        DOF = cms.required.string,
        cut = cms.required.double,
        sigCut = cms.required.double,
        maxMoveCut = cms.required.double,
        maxErrorCut = cms.required.double,
        fractionCut = cms.optional.double
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
