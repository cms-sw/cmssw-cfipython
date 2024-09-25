import FWCore.ParameterSet.Config as cms

def PixelClusterTagInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelClusterTagInfoProducer',
    jets = cms.InputTag('ak4PFJetsCHS'),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    pixelhit = cms.InputTag('siPixelClusters'),
    isPhase1 = cms.bool(True),
    addForward = cms.bool(True),
    minAdcCount = cms.int32(-1),
    minJetPtCut = cms.double(100),
    maxJetEtaCut = cms.double(2.5),
    hadronMass = cms.double(12),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
