import FWCore.ParameterSet.Config as cms

def MCMisalignmentScaler(**kwargs):
  mod = cms.EDAnalyzer('MCMisalignmentScaler',
    scalers = cms.VPSet(
      cms.PSet()
    ),
    pullBadModulesToIdeal = cms.untracked.bool(False),
    outlierPullToIdealCut = cms.untracked.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
