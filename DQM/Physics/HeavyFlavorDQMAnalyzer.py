import FWCore.ParameterSet.Config as cms

def HeavyFlavorDQMAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HeavyFlavorDQMAnalyzer',
    folder = cms.string('Physics/HeavyFlavor'),
    pvCollection = cms.required.InputTag,
    beamSpot = cms.required.InputTag,
    OniaToMuMuCands = cms.optional.InputTag,
    Kx0ToKPiCands = cms.optional.InputTag,
    PhiToKKCands = cms.optional.InputTag,
    BuToJPsiKCands = cms.optional.InputTag,
    BuToPsi2SKCands = cms.optional.InputTag,
    BdToJPsiKx0Cands = cms.optional.InputTag,
    BsToJPsiPhiCands = cms.optional.InputTag,
    K0sToPiPiCands = cms.optional.InputTag,
    Lambda0ToPPiCands = cms.optional.InputTag,
    BdToJPsiK0sCands = cms.optional.InputTag,
    LambdaBToJPsiLambda0Cands = cms.optional.InputTag,
    BcToJPsiPiCands = cms.optional.InputTag,
    Psi2SToJPsiPiPiCands = cms.optional.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
