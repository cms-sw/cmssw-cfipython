import FWCore.ParameterSet.Config as cms

def ParticleNetFeatureEvaluator(**kwargs):
  mod = cms.EDProducer('ParticleNetFeatureEvaluator',
    jet_radius = cms.double(0.8),
    min_jet_pt = cms.double(150),
    max_jet_eta = cms.double(99),
    min_jet_eta = cms.double(0),
    min_pt_for_track_properties = cms.double(-1),
    min_pt_for_pfcandidates = cms.double(-1),
    min_pt_for_losttrack = cms.double(1),
    max_dr_for_losttrack = cms.double(0.4),
    min_pt_for_taus = cms.double(20),
    max_eta_for_taus = cms.double(2.5),
    include_neutrals = cms.bool(True),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    secondary_vertices = cms.InputTag('slimmedSecondaryVertices'),
    pf_candidates = cms.InputTag('packedPFCandidates'),
    losttracks = cms.InputTag('lostTracks'),
    jets = cms.InputTag('slimmedJetsAK8'),
    muons = cms.InputTag('slimmedMuons'),
    taus = cms.InputTag('slimmedTaus'),
    electrons = cms.InputTag('slimmedElectrons'),
    photons = cms.InputTag('slimmedPhotons'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
