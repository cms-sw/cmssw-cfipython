import FWCore.ParameterSet.Config as cms

def AlignmentGoodIdMuonSelector(*args, **kwargs):
  mod = cms.EDFilter('AlignmentGoodIdMuonSelector',
    src = cms.InputTag('muons'),
    maxEta = cms.double(2.5),
    maxChi2 = cms.double(20),
    minMuonHits = cms.int32(0),
    minMatches = cms.int32(1),
    requireGlobal = cms.bool(True),
    requireTracker = cms.bool(True),
    useSecondarySelection = cms.bool(False),
    secondaryEtaLow = cms.double(2.3),
    secondaryEtaHigh = cms.double(3),
    secondaryMinMatches = cms.int32(0),
    secondaryRequireTracker = cms.bool(True),
    filter = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
