import FWCore.ParameterSet.Config as cms

def PATElectronUpdater(**kwargs):
  mod = cms.EDProducer('PATElectronUpdater',
    src = cms.required.InputTag,
    vertices = cms.required.InputTag,
    beamspot = cms.InputTag('offlineBeamSpot'),
    computeMiniIso = cms.bool(False),
    fixDxySign = cms.bool(False),
    pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
    miniIsoParamsB = cms.optional.vdouble,
    miniIsoParamsE = cms.optional.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
