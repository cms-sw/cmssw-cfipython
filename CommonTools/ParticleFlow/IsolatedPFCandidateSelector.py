import FWCore.ParameterSet.Config as cms

def IsolatedPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('IsolatedPFCandidateSelector',
    src = cms.InputTag(''),
    isolationValueMapsCharged = cms.VInputTag(),
    isolationValueMapsNeutral = cms.VInputTag(),
    doDeltaBetaCorrection = cms.bool(False),
    deltaBetaIsolationValueMap = cms.InputTag(''),
    deltaBetaFactor = cms.double(-0.5),
    isRelative = cms.bool(True),
    isolationCut = cms.double(999),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
