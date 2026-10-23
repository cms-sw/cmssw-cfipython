import FWCore.ParameterSet.Config as cms

def MuonTagInfoCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonTagInfoCollectionProducer',
    src = cms.InputTag('slimmedMuons'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    secondary_vertices = cms.InputTag('slimmedSecondaryVertices'),
    pvSrc = cms.InputTag('offlineSlimmedPrimaryVertices'),
    leptonVars = cms.PSet(
      allowAnyLabel_ = cms.optional.string
    ),
    pfVars = cms.PSet(
      allowAnyLabel_ = cms.optional.string
    ),
    svVars = cms.PSet(
      allowAnyLabel_ = cms.optional.string
    ),
    leptonVarsExt = cms.PSet(
      allowAnyLabel_ = cms.optional.InputTag
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
