import FWCore.ParameterSet.Config as cms

def PATMuonUpdater(*args, **kwargs):
  mod = cms.EDProducer('PATMuonUpdater',
    src = cms.required.InputTag,
    vertices = cms.required.InputTag,
    beamspot = cms.InputTag('offlineBeamSpot'),
    computeMiniIso = cms.bool(False),
    fixDxySign = cms.bool(False),
    pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
    recomputeMuonBasicSelectors = cms.bool(False),
    recomputeSoftMuonMvaRun3 = cms.bool(False),
    softMvaRun3Model = cms.string('RecoMuon/MuonIdentification/data/Run2022-20231030-1731-Event0'),
    miniIsoParams = cms.optional.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
