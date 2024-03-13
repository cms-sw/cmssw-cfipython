import FWCore.ParameterSet.Config as cms

TOoLLiPProducer = cms.EDProducer('TOoLLiPProducer',
  jets = cms.InputTag('scPFL1Puppi'),
  useRawPt = cms.bool(True),
  TOoLLiPVersion = cms.string('TOoLLiP_v1'),
  NNInput = cms.string('input:0'),
  NNOutput = cms.string('sequential/dense_2/Sigmoid'),
  maxJets = cms.int32(10),
  nParticles = cms.int32(10),
  minPt = cms.double(20),
  maxEta = cms.double(2.4),
  vtx = cms.InputTag('L1VertexFinderEmulator', 'L1VerticesEmulation'),
  mightGet = cms.optional.untracked.vstring
)
