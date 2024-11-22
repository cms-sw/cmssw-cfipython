import FWCore.ParameterSet.Config as cms

def PatJetConstituentTableProducer(*args, **kwargs):
  mod = cms.EDProducer('PatJetConstituentTableProducer',
    name = cms.string('JetPFCands'),
    nameSV = cms.string('JetSV'),
    idx_name = cms.string('candIdx'),
    idx_nameSV = cms.string('svIdx'),
    jet_radius = cms.double(1),
    readBtag = cms.bool(True),
    jets = cms.InputTag('slimmedJetsAK8'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    candidates = cms.InputTag('packedPFCandidates'),
    secondary_vertices = cms.InputTag('slimmedSecondaryVertices'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
