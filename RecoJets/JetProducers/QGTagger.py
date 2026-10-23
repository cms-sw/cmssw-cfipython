import FWCore.ParameterSet.Config as cms

def QGTagger(*args, **kwargs):
  mod = cms.EDProducer('QGTagger',
    srcJets = cms.InputTag('ak4PFJetsCHS'),
    srcRho = cms.InputTag('fixedGridRhoFastjetAll'),
    computeLikelihood = cms.bool(True),
    jetsLabel = cms.string('QGL_AK4PFchs'),
    systematicsLabel = cms.string(''),
    useQualityCuts = cms.bool(False),
    jec = cms.InputTag(''),
    srcVertexCollection = cms.InputTag('offlinePrimaryVerticesWithBS'),
    srcConstituentWeights = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
