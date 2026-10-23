import FWCore.ParameterSet.Config as cms

def AlignmentMuonSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentMuonSelectorModule',
    src = cms.InputTag(''),
    applyBasicCuts = cms.bool(True),
    applyNHighestPt = cms.bool(False),
    applyMultiplicityFilter = cms.bool(False),
    applyMassPairFilter = cms.bool(False),
    nHighestPt = cms.int32(2),
    minMultiplicity = cms.int32(1),
    pMin = cms.double(0),
    pMax = cms.double(999999),
    ptMin = cms.double(10),
    ptMax = cms.double(999999),
    etaMin = cms.double(-2.4),
    etaMax = cms.double(2.4),
    phiMin = cms.double(-3.1416),
    phiMax = cms.double(3.1416),
    nHitMinSA = cms.double(0),
    nHitMaxSA = cms.double(999999),
    chi2nMaxSA = cms.double(999999),
    nHitMinGB = cms.double(0),
    nHitMaxGB = cms.double(999999),
    chi2nMaxGB = cms.double(999999),
    nHitMinTO = cms.double(0),
    nHitMaxTO = cms.double(999999),
    chi2nMaxTO = cms.double(999999),
    minMassPair = cms.double(89),
    maxMassPair = cms.double(90),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
