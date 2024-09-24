import FWCore.ParameterSet.Config as cms

def L1TS2PFJetInputPatternWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TS2PFJetInputPatternWriter',
    nPayloadFrames = cms.untracked.uint32(40),
    nHeaderFrames = cms.untracked.uint32(1),
    inputCollectionTag = cms.InputTag('l1pfCandidates', 'Puppi', 'IN'),
    filename = cms.untracked.string('pattern.txt'),
    nChanPerQuad = cms.untracked.uint32(4),
    nClearFrames = cms.untracked.uint32(13),
    nQuads = cms.untracked.uint32(18),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
