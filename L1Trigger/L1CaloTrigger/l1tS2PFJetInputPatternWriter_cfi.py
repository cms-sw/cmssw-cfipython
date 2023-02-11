import FWCore.ParameterSet.Config as cms

l1tS2PFJetInputPatternWriter = cms.EDAnalyzer('L1TS2PFJetInputPatternWriter',
  nPayloadFrames = cms.untracked.uint32(40),
  nHeaderFrames = cms.untracked.uint32(1),
  inputCollectionTag = cms.InputTag('l1pfCandidates', 'Puppi', 'IN'),
  filename = cms.untracked.string('pattern.txt'),
  nChanPerQuad = cms.untracked.uint32(4),
  nClearFrames = cms.untracked.uint32(13),
  nQuads = cms.untracked.uint32(18),
  mightGet = cms.optional.untracked.vstring
)
