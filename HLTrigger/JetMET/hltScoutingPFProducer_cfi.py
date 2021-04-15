import FWCore.ParameterSet.Config as cms

hltScoutingPFProducer = cms.EDProducer('HLTScoutingPFProducer',
  pfJetCollection = cms.InputTag('hltAK4PFJets'),
  pfJetTagCollection = cms.InputTag('hltDeepCombinedSecondaryVertexBJetTagsPF'),
  pfCandidateCollection = cms.InputTag('hltParticleFlow'),
  vertexCollection = cms.InputTag('hltPixelVertices'),
  metCollection = cms.InputTag('hltPFMETProducer'),
  rho = cms.InputTag('hltFixedGridRhoFastjetAll'),
  pfJetPtCut = cms.double(20),
  pfJetEtaCut = cms.double(3),
  pfCandidatePtCut = cms.double(0.6),
  pfCandidateEtaCut = cms.double(5),
  mantissaPrecision = cms.int32(10),
  doJetTags = cms.bool(True),
  doCandidates = cms.bool(True),
  doMet = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
