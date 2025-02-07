import FWCore.ParameterSet.Config as cms

def MCMisalignmentScaler(*args, **kwargs):
  mod = cms.EDAnalyzer('MCMisalignmentScaler',
    scalers = cms.VPSet(
      cms.PSet()
    ),
    pullBadModulesToIdeal = cms.untracked.bool(False),
    outlierPullToIdealCut = cms.untracked.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
