import FWCore.ParameterSet.Config as cms

def QGTagger(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
