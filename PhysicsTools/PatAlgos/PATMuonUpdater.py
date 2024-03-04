import FWCore.ParameterSet.Config as cms

def PATMuonUpdater(**kwargs):
  mod = cms.EDProducer('PATMuonUpdater',
    src = cms.required.InputTag,
    vertices = cms.required.InputTag,
    beamspot = cms.InputTag('offlineBeamSpot'),
    computeMiniIso = cms.bool(False),
    fixDxySign = cms.bool(False),
    pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
    recomputeMuonBasicSelectors = cms.bool(False),
    miniIsoParams = cms.optional.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
