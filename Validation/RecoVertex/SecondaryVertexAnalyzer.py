import FWCore.ParameterSet.Config as cms

def SecondaryVertexAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('SecondaryVertexAnalyzer',
    rootFolder = cms.untracked.string('Validation/Vertices/Secondary'),
    verbose = cms.untracked.bool(False),
    ignoreMissingCollections = cms.untracked.bool(False),
    doGenericSimPlots = cms.untracked.bool(True),
    doPerPdgPlots = cms.untracked.bool(True),
    recoVertexCollections = cms.required.VInputTag,
    vertexAssociators = cms.required.VInputTag,
    primaryVertices = cms.required.InputTag,
    hepMCProduct = cms.InputTag('generatorSmeared'),
    simVertices = cms.InputTag('mix', 'MergedTrackTruth'),
    trackAssociation = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    minDecayLength = cms.double(0.01),
    maxDecayLength = cms.double(20),
    minPt = cms.double(10),
    minPtReconstructableDaughters = cms.double(0.5),
    minReconstructableDaughters = cms.int32(2),
    signalPdgIds = cms.vint32(),
    bHadrons = cms.bool(True),
    cHadrons = cms.bool(True),
    sHadrons = cms.bool(True),
    taus = cms.bool(True),
    otherParticles = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
